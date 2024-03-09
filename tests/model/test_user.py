from unittest import TestCase
from source.model.user import User


class TestUserModel(TestCase):

    def test_user_model_properties(self):
        username="foo"
        password="bar"

        user = User(username=username, password=password)

        self.assertEqual(username, user.username)
        self.assertEqual(password, user.password)
