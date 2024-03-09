from unittest import TestCase
from source.model.map import Map


class TestMapModel(TestCase):

    def test_map_model_properties(self):
        id="foo"
        path="bar"

        map = Map(id=id, path=path)

        self.assertEqual(id, map.id)
        self.assertEqual(path, map.path)
