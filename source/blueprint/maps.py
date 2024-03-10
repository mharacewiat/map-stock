from uuid import UUID
from flask import Blueprint, jsonify, request
from source.gateway.message import MessageGateway
from source.handler.map_upload import MapUploadHandler
from source.repository.map import MapRepository
from injector import inject

bp = Blueprint("maps", __name__, url_prefix="/api/v1/maps")


@bp.route("/", methods=["POST"])
@inject
def post(map_upload_handler: MapUploadHandler, message_gateway: MessageGateway):
    map = map_upload_handler.upload(request.files["file"])

    return jsonify(map.model_dump())


@bp.route("/<uuid:id>", methods=["GET"])
@inject
def get(id: UUID, map_repository: MapRepository):
    map = map_repository.get_map(id)
    # map.is_public = 1
    map_repository.save_map(map)

    if not map.is_public:
        raise Exception()

    return jsonify(map.model_dump())
