from boto3.dynamodb.types import TypeSerializer
from boto3.dynamodb.types import TypeDeserializer
from injector import inject


class Boto3Serializer:

    @inject
    def __init__(self, serializer: TypeSerializer, deserializer: TypeDeserializer):
        self.serializer = serializer
        self.deserializer = deserializer

    def serialize(self, data: dict) -> dict:
        """
        Serializes regular dict into boto3-specific dict.

        Args:
            data (dict): Regular dic

        Returns:
            dict: boto3-specific dict
        """
        
        return {k: self.serializer.serialize(v) for k, v in data.items()}

    def deserialize(self, data: dict) -> dict:
        """
        Deserializes boto3-specific dict into regular dict.

        Args:
            data (dict): boto3-specific dict

        Returns:
            dict: Regular dict
        """
        
        return {k: self.deserializer.deserialize(v) for k, v in data.items()}
