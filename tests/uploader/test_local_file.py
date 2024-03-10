from unittest import TestCase
from unittest.mock import Mock
from werkzeug.datastructures import FileStorage
from source.uploader.local_file import LocalFileUploader


class TestLocalFileUploader(TestCase):

    def test_upload(self):
        file_mock = Mock(spec=FileStorage)

        local_file_uploader = LocalFileUploader("/foo/bar/baz")
        file_path = local_file_uploader.upload("qux", file_mock)

        self.assertEqual("/foo/bar/baz/qux", file_path)
