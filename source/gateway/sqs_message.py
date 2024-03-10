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

    def notify(self, map: Map) -> None:
        self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=map.model_dump_json(),
        )
