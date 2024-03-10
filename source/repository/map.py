from abc import ABCMeta
from uuid import UUID
from source.model.map import Map


class MapRepository(metaclass=ABCMeta):

    def get_map(self, id: UUID) -> Map:
        """
        Get map.

        Args:
            id (UUID): The identifier of a map

        Returns:
            Map: The map
        """

        pass

    def save_map(self, map: Map) -> Map:
        """
        Create or update map

        Args:
            map (Map): The map to create or update

        Returns:
            Map: The created or updated map
        """

        pass
