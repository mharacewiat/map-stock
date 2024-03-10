from unittest import TestCase
from source.model.map import Map


class TestMapModel(TestCase):

    def test_map_model_properties(self):
        id="foo"
        file_path="bar"
        is_processed=0
        is_public=1

        map = Map(id=id, file_path=file_path, is_processed=is_processed, is_public=is_public)

        self.assertEqual(id, map.id)
        self.assertEqual(file_path, map.file_path)
        self.assertEqual(is_processed, map.is_processed)
        self.assertEqual(is_public, map.is_public)
