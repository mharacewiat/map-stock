from abc import ABCMeta
from source.model.map import Map


class MapRepository(metaclass=ABCMeta):

    def get_map(self, id: str) -> Map:
        pass

    def save_map(self, map: Map) -> Map:
        pass
