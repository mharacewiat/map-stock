from flask import Blueprint, jsonify, request, current_app
from injector import inject
from pydantic import ValidationError
from source.authorizer.user import UserAuthorizer

from source.model.authorization_request import AuthorizationRequestModel
from source.repository.dynamo_db_user import DynamoDbUserRepository


bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@bp.route("/", methods=["POST"])
@inject
def token(user_authorizer: UserAuthorizer):
    try:
        authorization_request = AuthorizationRequestModel(**request.get_json())
    except ValidationError as e:
        current_app.logger.debug(e.errors())
        return e.errors(), 400

    try:
        access_token, ttl = user_authorizer.authorize(
            authorization_request.username, authorization_request.password
        )
    except Exception as e:
        current_app.logger.debug(str(e))
        return jsonify(error="Permission denied."), 404

    return jsonify(access_token=access_token, ttl=ttl)
