from unittest import TestCase
from unittest.mock import Mock
from source.gateway.sqs_message import SqsMessageGateway
from source.model.map import Map


class TestSqsMessageGateway(TestCase):

    def test_success(self):
        client_mock = Mock()
        client_mock.send_message.return_value = {}

        queue_url = "http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/maps-uploaded"

        sqs_message_gateway = SqsMessageGateway(
            queue_url=queue_url,
            client=client_mock,
        )

        map = Map(file_path="/foo/bar/baz", is_processed=0, is_public=1)
        sqs_message_gateway.send(map)

        client_mock.send_message.assert_called_once_with(
            QueueUrl=queue_url,
            MessageBody=map.model_dump_json(),
        )
