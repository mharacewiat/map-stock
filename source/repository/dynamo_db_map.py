from injector import inject, noninjectable
from source.model.map import Map
from source.repository.map import MapRepository
from boto3 import client
from source.serializer.boto3 import Boto3Serializer
from flask import current_app


class DynamoDbMapRepository(MapRepository):
    
    @inject
    @noninjectable("client")
    def __init__(self, client: client, serializer: Boto3Serializer):
        self.client = client
        self.serializer = serializer

    def get_map(self, id: str) -> Map:
        response = self.client.get_item(
            TableName='maps',
            Key={"id": {"S": id}}
        )
        
        if response.get("ResponseMetadata").get("HTTPStatusCode") != 200 or not "Item" in response:
            raise Exception("Map not found")
        
        return Map(**self.serializer.deserialize(response.get("Item")))

    def save_map(self, map: Map) -> Map:
        data = {f":{k}": v for k, v in map.model_dump().items()}
        del data[":id"]
        
        response = self.client.update_item(
            TableName='maps',
            Key={"id": {"S": map.id}},
            UpdateExpression="SET file_path=:file_path, is_processed=:is_processed, is_public=:is_public",
            ExpressionAttributeValues=self.serializer.serialize(data)
        )
        
        if response.get("ResponseMetadata").get("HTTPStatusCode") != 200:
            raise Exception("Failed to save map")
        
        return map
