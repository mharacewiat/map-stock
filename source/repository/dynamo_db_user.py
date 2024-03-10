from injector import inject, noninjectable
from source.model.user import User
from source.repository.user import UserRepository
from boto3 import client
from source.serializer.boto3 import Boto3Serializer


class DynamoDbUserRepository(UserRepository):

    @inject
    @noninjectable("client")
    def __init__(self, client: client, serializer: Boto3Serializer):
        self.client = client
        self.serializer = serializer

    def get_user(self, username: str) -> User:
        response = self.client.get_item(
            TableName='users',
            Key={"id": {"S": id}}
        )
        
        if response.get("ResponseMetadata").get("HTTPStatusCode") != 200 or not "Item" in response:
            raise Exception("User not found")
        
        return User(**self.serializer.deserialize(response.get("Item")))

    def save_user(self, user: User) -> User:
        data = {f":{k}": v for k, v in user.model_dump().items()}
        del data[":username"]
        
        response = self.client.update_item(
            TableName='users',
            Key={"username": {"S": user.username}},
            UpdateExpression="SET password=:password, is_active=:is_active",
            ExpressionAttributeValues=self.serializer.serialize(data)
        )
        
        if response.get("ResponseMetadata").get("HTTPStatusCode") != 200:
            raise Exception("Failed to save user")
        
        return user
