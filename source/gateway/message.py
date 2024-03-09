from abc import ABCMeta
from source.model.map import Map


class MessageGateway(metaclass=ABCMeta):

    def notify(self, map: Map) -> None:
        pass
