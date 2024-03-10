from uuid import UUID
from flask import Blueprint, jsonify, request, current_app, abort, send_file
from source.gateway.message import MessageGateway
from source.handler.map_upload import MapUploadHandler
from source.model.upload_request import UploadRequestModel
from source.repository.dynamo_db_user import DynamoDbUserRepository
from source.repository.map import MapRepository
from injector import inject
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from pydantic import ValidationError

from source.repository.user import UserRepository

bp = Blueprint("maps", __name__, url_prefix="/api/v1/maps")


@bp.route("/", methods=["POST"])
@inject
@jwt_required()
def post(user_repository: UserRepository, map_upload_handler: MapUploadHandler):
    try:
        upload_request = UploadRequestModel(**request.files)
    except ValidationError as e:
        current_app.logger.debug(e.errors())
        return e.errors(), 400

    user = user_repository.get_user(get_jwt_identity())
    if not user.is_active:
        return jsonify(error="Only active users can upload movies"), 404

    try:
        map = map_upload_handler.upload(upload_request.file)
    except Exception as e:
        current_app.logger.debug(str(e))
        return jsonify(error="Error uploading a file."), 500

    return jsonify(map.model_dump())


@bp.route("/<uuid:id>", methods=["GET"])
@inject
def get(id: UUID, map_repository: MapRepository):
    map = map_repository.get_map(id)

    if not map.is_processed:
        current_app.logger.warning("Attempted to view not processed map")
        return jsonify(error="The map is not processed"), 404
        
    if not map.is_public:
        try:
            verify_jwt_in_request(fresh=True)
        except Exception:
            current_app.logger.warning("Attempted to view private map as guest")
            return jsonify(error="The map is private"), 404

    return send_file(map.file_path)
