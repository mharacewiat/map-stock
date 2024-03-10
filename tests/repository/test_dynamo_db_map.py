from unittest import TestCase
from unittest.mock import MagicMock, Mock
from uuid import UUID
from source.model.map import Map
from source.repository.dynamo_db_map import DynamoDbMapRepository
from source.serializer.boto3 import Boto3Serializer
from boto3 import client


class TestDynamoDbMapRepository(TestCase):
    
    def test_get_map(self):
        id=UUID("50b990c5-a322-491d-a2ee-d5b322d3b478")
        file_path="/foo/bar/baz"
        is_public=1
        is_processed=1
        
        item = {
            "is_processed": {"N": str(is_processed)}, 
            "is_public": {"N": str(is_public)}, 
            "file_path": {"S": file_path}, 
            "id": {"S": str(id)}
        }
        
        client_mock = MagicMock()
        client_mock.get_item.return_value={
            "Item": item, 
            "ResponseMetadata": {
                "HTTPStatusCode": 200
            }
        }
        
        serialiezer_mock = Mock(spec=Boto3Serializer)
        serialiezer_mock.deserialize.return_value={
            "is_processed": is_processed,
            "is_public": is_public,
            "file_path": file_path,
            "id": id
        }

        dynamodb_map_repository = DynamoDbMapRepository(
            client=client_mock,
            serializer=serialiezer_mock
        )

        map = dynamodb_map_repository.get_map(id)

        self.assertEqual(map.id, id)
        self.assertEqual(map.file_path, file_path)
        self.assertEqual(map.is_public, is_public)
        self.assertEqual(map.is_processed, is_processed)
        
        client_mock.get_item.assert_called_once()
        serialiezer_mock.deserialize.assert_called_once_with(item)

    def test_get_map_exception(self):
        client_mock = MagicMock()
        client_mock.get_item.return_value={
            "ResponseMetadata": {
                "HTTPStatusCode": 0
            }
        }
        
        serialiezer_mock = Mock(spec=Boto3Serializer)
        
        dynamodb_map_repository = DynamoDbMapRepository(
            client=client_mock,
            serializer=serialiezer_mock
        )
        
        with self.assertRaises(Exception):
            dynamodb_map_repository.get_map(123)
            
        client_mock.get_item.assert_called_once()
        serialiezer_mock.deserialize.assert_not_called()
    
    def test_save_map(self):
        file_path="/foo/bar/baz"
        is_processed=0
        is_public=1
        
        map = Map(file_path=file_path, is_processed=is_processed, is_public=is_public)
        id = map.id
        
        client_mock = MagicMock()
        client_mock.update_item.return_value={
            "ResponseMetadata": {
                "HTTPStatusCode": 200
            }
        }
        
        
        serialiezer_mock = Mock(spec=Boto3Serializer)
        serialiezer_mock.serialize.return_value={
            ":id": {"S": id}, 
            ":file_path": {"S": file_path}, 
            ":is_processed": {"N": str(is_processed)}, 
            ":is_public": {"N": str(is_public)}
        }

        dynamodb_map_repository = DynamoDbMapRepository(
            client=client_mock,
            serializer=serialiezer_mock
        )

        returned_map = dynamodb_map_repository.save_map(map)

        self.assertEqual(returned_map.id, id)
        self.assertEqual(returned_map.file_path, file_path)
        self.assertEqual(returned_map.is_processed, is_processed)
        self.assertEqual(returned_map.is_public, is_public)
        
        client_mock.update_item.assert_called_once()
        serialiezer_mock.serialize.assert_called_once_with({
            ":file_path": file_path, 
            ":is_processed": is_processed, 
            ":is_public": is_public
        })

    def test_save_map_exception(self):
        map = Map(file_path="/foo/bar/baz",is_processed=0,is_public=1)
        
        client_mock = MagicMock()
        client_mock.update_item.return_value={
            "ResponseMetadata": {
                "HTTPStatusCode": 0
            }
        }
        
        serialiezer_mock = Mock(spec=Boto3Serializer)

        dynamodb_map_repository = DynamoDbMapRepository(
            client=client_mock,
            serializer=serialiezer_mock
        )

        with self.assertRaises(Exception):
            dynamodb_map_repository.save_map(map)

        client_mock.update_item.assert_called_once()
