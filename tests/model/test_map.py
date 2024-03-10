from unittest import TestCase
from uuid import UUID
from source.model.map import Map


class TestMapModel(TestCase):

    def test_map_model_properties(self):
        file_path = "bar"
        is_processed = 0
        is_public = 1

        map = Map(file_path=file_path, is_processed=is_processed, is_public=is_public)

        self.assertIsInstance(map.id, UUID)
        self.assertEqual(file_path, map.file_path)
        self.assertEqual(is_processed, map.is_processed)
        self.assertEqual(is_public, map.is_public)
