from injector import Module
from source.gateway.message import MessageGateway
from source.handler.map_upload import MapUploadHandler
from source.repository.map import MapRepository
from source.repository.user import UserRepository
from source.uploader.file import FileUploader
from source.authorizer.user import UserAuthorizer


class Container(Module):
    
    def configure(self, binder):
        binder.bind(UserAuthorizer, type("DummyUserAuthorizer", (UserAuthorizer), {}))
        binder.bind(MessageGateway, type("DummyMessageGateway", (MessageGateway), {}))
        binder.bind(MapUploadHandler, type("DummyMapUploadHandler", (MapUploadHandler), {}))
        binder.bind(MapRepository, type("DummyMapRepository", (MapRepository), {}))
        binder.bind(UserRepository, type("DummyUserRepository", (UserRepository), {}))
        binder.bind(FileUploader, type("DummyFileUploader", (FileUploader), {}))
