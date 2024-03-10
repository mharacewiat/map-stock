from typing import Tuple
from source.model.user import User
from injector import inject
from source.repository.user import UserRepository
from flask import current_app
from flask_jwt_extended import create_access_token
from datetime import timedelta
from bcrypt import hashpw, checkpw, gensalt


class UserAuthorizer:

    @inject
    def __init__(self, user_repository: UserRepository, ttl: int = 900) -> None:
        self.user_repository = user_repository
        self.ttl = ttl

    def authorize(self, username: str, password: str) -> str:
        user = self.user_repository.get_user(username)
        user.password = hashpw(password.encode(), gensalt()).decode()

        if not checkpw(password.encode(), user.password.encode()):
            raise Exception()

        return self.encode_jwt_token(user)

    def encode_jwt_token(self, user: User) -> Tuple[str, int]:
        token = create_access_token(
            identity=user.username,
            expires_delta=timedelta(seconds=self.ttl),
        )

        return token, self.ttl
