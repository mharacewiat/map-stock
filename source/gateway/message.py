from abc import ABCMeta
from source.model.map import Map


class MessageGateway(metaclass=ABCMeta):

    def send(self, map: Map) -> None:
        """
        Send a message for further processing by third-party app.

        Args:
            map (Map): The map details
        """
        
        pass

    def receive(self) -> Map:
        """
        A simulation for a third-party app. Receive the message necessary to process map.

        Returns:
            Map: Processing-pending map object
        """

        pass
