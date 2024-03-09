from unittest import TestCase
from unittest.mock import Mock
from source.gateway.message import MessageGateway
from source.handler.map_upload import MapUploadHandler
from source.model.map import Map
from source.repository.map import MapRepository
from source.uploader.file import FileUploader


class TestMapUploadHandler(TestCase):
    
    def test_success(self):
        file="XYZ"
        path= "/foo/bar/baz"
        file_uploader_mock = Mock(spec=FileUploader)
        file_uploader_mock.upload.return_value=path

        map = Map(id="XYZ",path=path)
        map_repository_mock = Mock(spec=MapRepository)
        map_repository_mock.save_map.return_value=map

        message_gateway_mock = Mock(spec=MessageGateway)

        map_uploader = MapUploadHandler(
            file_uploader=file_uploader_mock, 
            map_repository=map_repository_mock,
            message_gateway=message_gateway_mock
        )


        resulted_map = map_uploader.upload(file)

        self.assertEqual(map, resulted_map)
        file_uploader_mock.upload.assert_called_once_with(file)
        map_repository_mock.save_map.assert_called_once()
        message_gateway_mock.notify.assert_called_once_with(map)
