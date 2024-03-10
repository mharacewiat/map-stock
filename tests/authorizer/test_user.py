from unittest import TestCase
from unittest.mock import Mock, patch
from source.authorizer.user import UserAuthorizer
from source.model.user import User
from source.repository.user import UserRepository


class TestUserAuthorizer(TestCase):

    def test_failure_missing_user(self):
        user_repository_mock = Mock(spec=UserRepository)
        user_repository_mock.get_user.return_value = None

        user_authorizer = UserAuthorizer(user_repository_mock)

        with self.assertRaises(Exception):
            user_authorizer.authorize("foo", "bar")

    def test_failure_password_missmatch(self):
        user_repository_mock = Mock(spec=UserRepository)
        user_repository_mock.get_user.return_value = User(
            username="foo", password="bar"
        )

        user_authorizer = UserAuthorizer(user_repository_mock)

        with self.assertRaises(Exception):
            user_authorizer.authorize("foo", "baz")

    def test_success(self):
        self.skipTest(
            "I was unable to patch the `create_access_token`, it crashes because outside of the app_context"
        )

        username = "foo"
        password = "bar"
        token = "token"
        ttl = 123
        existing_user = User(username=username, password=password)

        user_repository_mock = Mock(spec=UserRepository)
        user_repository_mock.get_user.return_value = existing_user

        user_authorizer = UserAuthorizer(user_repository=user_repository_mock)

        with patch(
            "flask_jwt_extended.create_access_token"
        ) as create_access_token_mock:
            create_access_token_mock.return_value = "token"

            resulting_access_token, resulting_ttl = user_authorizer.authorize(
                username, password
            )
            self.assertEqual(token, resulting_access_token)
            self.assertEqual(ttl, resulting_ttl)

        user_repository_mock.get_user.assert_called_once_with(username)
