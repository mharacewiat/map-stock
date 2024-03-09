from unittest import TestCase
from unittest.mock import Mock

from source.authorizer.user import UserAuthorizer
from source.model.user import User
from source.repository.user import UserRepository


class TestUserAuthorizer(TestCase):
    
    def test_failure_missing_user(self):
        user_repository_mock = Mock(spec=UserRepository)
        user_repository_mock.get_user.return_value=None

        user_authorizer = UserAuthorizer(user_repository_mock)

        with self.assertRaises(Exception):
            user_authorizer.authroize("foo", "bar")

    def test_failure_password_missmatch(self):
        user_repository_mock = Mock(spec=UserRepository)
        user_repository_mock.get_user.return_value=User(username="foo", password="bar")

        user_authorizer = UserAuthorizer(user_repository_mock)

        with self.assertRaises(Exception):
            user_authorizer.authroize("foo", "baz")

    def test_success(self):
        username= "foo"
        password= "bar"
        existing_user = User(username=username, password=password)

        user_repository_mock = Mock(spec=UserRepository)
        user_repository_mock.get_user.return_value=existing_user

        user_authorizer = UserAuthorizer(user_repository_mock)
        authorized_user = user_authorizer.authroize("foo", "bar")

        user_repository_mock.get_user.assert_called_once_with("foo")
        self.assertEqual(existing_user.username, authorized_user.username)
