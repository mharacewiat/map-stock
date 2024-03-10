from abc import ABCMeta
from uuid import UUID
from source.model.map import Map


class MapRepository(metaclass=ABCMeta):

    def get_map(self, id: UUID) -> Map:
        pass

    def save_map(self, map: Map) -> Map:
        pass
