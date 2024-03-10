from source.gateway.message import MessageGateway
from injector import inject, noninjectable
from boto3 import client
from source.model.map import Map


class SqsMessageGateway(MessageGateway):

    @inject
    @noninjectable("queue_url")
    @noninjectable("client")
    def __init__(self, queue_url: str, client: client):
        self.queue_url = queue_url
        self.client = client

    def send(self, map: Map) -> None:
        self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=map.model_dump_json(),
        )

    def receive(self) -> Map:
        response = self.client.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=1,
            MessageAttributeNames=["All"],
            VisibilityTimeout=0,
            WaitTimeSeconds=0,
        )

        if (
            response.get("ResponseMetadata").get("HTTPStatusCode") != 200
            or not "Messages" in response
        ):
            raise Exception("No messages")

        message = response.get("Messages")[0]
        map = Map.parse_raw(message.get("Body"))

        self.client.delete_message(
            QueueUrl=self.queue_url, ReceiptHandle=message.get("ReceiptHandle")
        )

        return map
