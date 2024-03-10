from unittest import TestCase
from unittest.mock import Mock
from boto3.dynamodb.types import TypeSerializer
from boto3.dynamodb.types import TypeDeserializer
from source.serializer.boto3 import Boto3Serializer


class TestBoto3Serializer(TestCase):
    
    def test_serialize(self):
        serializer_mock = Mock(spec=TypeSerializer)
        serializer_mock.serialize.return_value={"S":"bar"}
        
        deserializer_mock = Mock(spec=TypeDeserializer)
        
        boto3_serializer = Boto3Serializer(serializer=serializer_mock, deserializer=deserializer_mock)
        
        output = boto3_serializer.serialize({"foo":"bar"})
        
        self.assertEqual({"S": "bar"}, output.get("foo"))
        
        deserializer_mock.deserialize.assert_not_called()
        
    # def test_serialize(self):
    #     serializer_mock = Mock(spec=TypeSerializer)
    #     serializer_mock.serialize.return_value="bar"
        
    #     deserializer_mock = Mock(spec=TypeDeserializer)
        
    #     boto3_serializer = Boto3Serializer(serializer=serializer_mock, deserializer=deserializer_mock)
        
    #     output = boto3_serializer.deserialize({"S": "bar"})
        
    #     self.assertEqual("bar", output.get("foo"))
        
    #     serializer_mock.deserialize.assert_not_called()
