from flask import Blueprint, jsonify


bp = Blueprint("maps", __name__, url_prefix="/api/v1/maps")

@bp.route("/", methods=["POST"])
def post():
    return jsonify("dummy")

@bp.route("/<string:id>", methods=["GET"])
def get(id: str):
    return jsonify(f"dummy-{id}")
