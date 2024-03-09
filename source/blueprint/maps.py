from flask import Blueprint, jsonify
from source.gateway.message import MessageGateway
from source.handler.map_upload import MapUploadHandler
from source.repository.map import MapRepository
from injector import inject


bp = Blueprint("maps", __name__, url_prefix="/api/v1/maps")


@bp.route("/", methods=["POST"])
@inject
def post(map_upload_handler: MapUploadHandler, message_gateway: MessageGateway):
    map = map_upload_handler.upload("XYZ")

    return jsonify(map.model_dump())

@bp.route("/<string:id>", methods=["GET"])
@inject
def get(id: str, map_repository: MapRepository):
    map = map_repository.get_map(id)

    return jsonify(map.model_dump())
