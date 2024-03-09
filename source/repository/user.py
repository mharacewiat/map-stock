from abc import ABCMeta
from source.model.user import User


class UserRepository(metaclass=ABCMeta):

    def get_user(self, username: str) -> User:
        pass
