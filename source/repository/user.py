from abc import ABCMeta
from source.model.user import User


class UserRepository(metaclass=ABCMeta):

    def get_user(self, username: str) -> User:
        """
        Get user.

        Args:
            username (str): The identifier of a user

        Returns:
            User: The user
        """

        pass

    def save_user(self, user: User) -> User:
        """
        Create or update user.

        Args:
            user (User): The user to create or update

        Returns:
            User: The created or updated user
        """

        pass
