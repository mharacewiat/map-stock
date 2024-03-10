from flask import Flask
from injector import Module
from source.authorizer.user import UserAuthorizer
from source.gateway.message import MessageGateway
from source.gateway.sqs_message import SqsMessageGateway
from source.handler.map_upload import MapUploadHandler
from source.repository.map import MapRepository
from source.repository.dynamo_db_map import DynamoDbMapRepository
from source.repository.user import UserRepository
from source.repository.dynamo_db_user import DynamoDbUserRepository
from source.serializer.boto3 import Boto3Serializer
from source.uploader.file import FileUploader
from source.uploader.local_file import LocalFileUploader
from boto3 import Session
from boto3.dynamodb.types import TypeSerializer
from boto3.dynamodb.types import TypeDeserializer


class Container(Module):

    def configure(self, binder):
        binder.bind(UserAuthorizer, UserAuthorizer)
        binder.bind(MapUploadHandler, MapUploadHandler)
        binder.bind(Boto3Serializer, Boto3Serializer)
        binder.bind(FileUploader, LocalFileUploader("/tmp"))
        binder.bind(TypeSerializer, TypeSerializer)
        binder.bind(TypeDeserializer, TypeDeserializer)

        with binder.injector.get(Flask).app_context() as app_context:
            config = app_context.app.config

            session = Session(
                region_name=config["AWS_REGION_NAME"], 
                aws_access_key_id=config["AWS_ACCESS_KEY_ID"],
                aws_secret_access_key=config["AWS_SECRET_ACCESS_KEY"],
            )

            sqs_client = session.client(
                "sqs", endpoint_url=config["AWS_ENDPOINT_URL"]
            )

            binder.bind(
                MessageGateway,
                SqsMessageGateway(
                    queue_url=config["AWS_QUEUE_URL"],
                    client=sqs_client,
                ),
            )

            dynamodb_client = session.client(
                "dynamodb", endpoint_url=config["AWS_ENDPOINT_URL"]
            )

            binder.bind(
                MapRepository,
                DynamoDbMapRepository(
                    client=dynamodb_client, 
                    serializer=binder.injector.create_object(Boto3Serializer),
                ),
            )
            binder.bind(
                UserRepository,
                DynamoDbUserRepository(
                    client=dynamodb_client,
                    serializer=binder.injector.create_object(Boto3Serializer),
                ),
            )
