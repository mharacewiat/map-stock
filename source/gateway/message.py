from abc import ABCMeta
from source.model.map import Map


class MessageGateway(metaclass=ABCMeta):

    def send(self, map: Map) -> None:
        pass

    def receive(self) -> Map:
        pass
