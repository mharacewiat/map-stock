from unittest import TestCase
from source.model.user import User


class TestUserModel(TestCase):

    def test_user_model_properties(self):
        username="foo"
        password="bar"
        is_active=1

        user = User(username=username, password=password, is_active=is_active)

        self.assertEqual(username, user.username)
        self.assertEqual(password, user.password)
        self.assertEqual(is_active, user.is_active)
