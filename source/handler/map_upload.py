from source.gateway.message import MessageGateway
from source.model.map import Map
from source.repository.map import MapRepository
from source.uploader.file import FileUploader
from injector import inject


class MapUploadHandler():

    @inject
    def __init__(
        self,
        file_uploader: FileUploader,
        map_repository: MapRepository, 
        message_gateway: MessageGateway
    )-> None:
        self.file_uploader = file_uploader
        self.map_repository = map_repository
        self.message_gateway = message_gateway


    def upload(self, file) -> Map:
        path = self.file_uploader.upload(file)
        map = Map(id="XYZ", path=path)

        map = self.map_repository.save_map(map)
        self.message_gateway.notify(map)

        return map
