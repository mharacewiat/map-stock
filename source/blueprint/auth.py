from flask import Blueprint, jsonify
from injector import inject
from source.authorizer.user import UserAuthorizer


bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@bp.route("/", methods=["POST"])
@inject
def token(user_authorizer: UserAuthorizer):
    access_token = user_authorizer.authorize("XYZ", "XYZ")

    return jsonify(access_token=access_token)
