from werkzeug.datastructures import FileStorage
from source.gateway.message import MessageGateway
from source.model.map import Map
from source.repository.map import MapRepository
from source.uploader.file import FileUploader
from injector import inject


class MapUploadHandler:

    @inject
    def __init__(
        self,
        file_uploader: FileUploader,
        map_repository: MapRepository,
        message_gateway: MessageGateway,
    ) -> None:
        self.file_uploader = file_uploader
        self.map_repository = map_repository
        self.message_gateway = message_gateway

    def upload(self, file: FileStorage) -> Map:
        """
        A serivce acting as upload orchestrator.

        Args:
            file (FileStorage): Source file

        Returns:
            Map: Resulting map object
        """
        
        map = Map(file_path="", is_processed=0, is_public=1)
        file_path = self.file_uploader.upload(str(map.id), file)
        map.file_path = file_path

        map = self.map_repository.save_map(map)
        self.message_gateway.send(map)

        return map
