from abc import ABCMeta
from werkzeug.datastructures import FileStorage


class FileUploader(metaclass=ABCMeta):

    def upload(self, filename: str, file: FileStorage) -> str:
        """
        File uploader.

        Args:
            filename (str): Filename of a destination
            file (FileStorage): Source file

        Returns:
            str: Complete file path
        """
        
        pass
