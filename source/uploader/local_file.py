from source.uploader.file import FileUploader
from werkzeug.datastructures import FileStorage
from os.path import join
from flask import current_app

class LocalFileUploader(FileUploader):

    def __init__(self, upload_directory: str):
        self.upload_directory = upload_directory

    def upload(self, filename: str, file: FileStorage) -> str: 
        file_path = join(self.upload_directory, filename)
        file.save(file_path)
        
        return file_path
