from source.model.user import User
from injector import inject
from source.repository.user import UserRepository


class UserAuthorizer:

    @inject
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def authroize(self, username: str, password: str) -> User:
        user = self.user_repository.get_user(username)

        # TODO: hashing
        if user == None or user.password != password:
            raise Exception()

        return user
