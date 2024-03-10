from pydantic import BaseModel


class AuthorizationRequestModel(BaseModel):

    username: str
    password: str
