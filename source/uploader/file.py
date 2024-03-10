from abc import ABCMeta
from werkzeug.datastructures import FileStorage


class FileUploader(metaclass=ABCMeta):

    def upload(self, filename: str, file: FileStorage) -> str:
        pass
