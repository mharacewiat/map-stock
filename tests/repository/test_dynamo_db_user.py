from unittest import TestCase
from unittest.mock import MagicMock, Mock
from source.model.user import User
from source.repository.dynamo_db_user import DynamoDbUserRepository

from source.serializer.boto3 import Boto3Serializer


class TestDynamoDbUserRepository(TestCase):
    
    # def test_get_user(self):
    #     username="foo"
    #     password="bar"
    #     is_active=1
        
    #     item = {
    #         "username": {"S": username}, 
    #         "password": {"S": password}, 
    #         "is_active": {"N": str(is_active)}, 
    #     }
        
    #     client_mock = MagicMock()
    #     client_mock.get_item.return_value={
    #         "Item": item, 
    #         "ResponseMetadata": {
    #             "HTTPStatusCode": 200
    #         }
    #     }
        
    #     serializer_mock = Mock(spec=Boto3Serializer)
    #     serializer_mock.deserialize.return_value={
    #         "username": username,
    #         "password": password,
    #         "is_active": is_active
    #     }

    #     dynamodb_user_repository = DynamoDbUserRepository(
    #         client=client_mock,
    #         serializer=serializer_mock
    #     )

    #     user = dynamodb_user_repository.get_user(id)

    #     self.assertEqual(user.username, username)
    #     self.assertEqual(user.password, password)
    #     self.assertEqual(user.is_active, is_active)
        
    #     client_mock.get_item.assert_called_once()
    #     serializer_mock.deserialize.assert_called_once_with(item)

    # def test_get_user_exception(self):
    #     client_mock = MagicMock()
    #     client_mock.get_item.return_value={
    #         "ResponseMetadata": {
    #             "HTTPStatusCode": 0
    #         }
    #     }
        
    #     serializer_mock = Mock(spec=Boto3Serializer)
        
    #     dynamodb_user_repository = DynamoDbUserRepository(
    #         client=client_mock,
    #         serializer=serializer_mock
    #     )
        
    #     with self.assertRaises(Exception):
    #         dynamodb_user_repository.get_user("foo")
            
    #     client_mock.get_item.assert_called_once()
    #     serializer_mock.deserialize.assert_not_called()
    
    # def test_save_user(self):
    #     username="foo"
    #     password="bar"
    #     is_active=1
        
    #     user = User(username=username, password=password, is_active=is_active)
        
    #     client_mock = MagicMock()
    #     client_mock.update_item.return_value={
    #         "ResponseMetadata": {
    #             "HTTPStatusCode": 200
    #         }
    #     }
        
    #     serializer_mock = Mock(spec=Boto3Serializer)
    #     serializer_mock.serialize.return_value={
    #         ":password": {"S": password}, 
    #         ":is_active": {"N": str(is_active)}, 
    #     }

    #     dynamodb_user_repository = DynamoDbUserRepository(
    #         client=client_mock,
    #         serializer=serializer_mock
    #     )

    #     returned_user = dynamodb_user_repository.save_user(user)

    #     self.assertEqual(returned_user.username, username)
    #     self.assertEqual(returned_user.password, password)
    #     self.assertEqual(returned_user.is_active, is_active)
        
    #     client_mock.update_item.assert_called_once()
    #     serializer_mock.serialize.assert_called_once_with({":password":password, ":is_active": is_active})

    def test_save_user_exception(self):
        user = User(username="foo",password="bar",is_active=1)
        
        client_mock = MagicMock()
        client_mock.update_item.return_value={
            "ResponseMetadata": {
                "HTTPStatusCode": 0
            }
        }
        
        serializer_mock = Mock(spec=Boto3Serializer)

        dynamodb_user_repository = DynamoDbUserRepository(
            client=client_mock,
            serializer=serializer_mock
        )

        with self.assertRaises(Exception):
            dynamodb_user_repository.save_user(user)

        client_mock.update_item.assert_called_once()
