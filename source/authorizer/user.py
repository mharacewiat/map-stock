from abc import ABCMeta, abstractclassmethod
from source.model.user import User


class UserAuthorizer(metaclass=ABCMeta):

    @abstractclassmethod
    def authroize(self, username: str, password: str) -> User:
        pass
