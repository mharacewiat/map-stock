
from abc import ABCMeta


class FileUploader(metaclass=ABCMeta):

    def upload(self, file) -> str: 
        pass
