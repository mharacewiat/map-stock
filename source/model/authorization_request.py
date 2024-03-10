from pydantic import BaseModel


class AuthorizationRequestModel(BaseModel):
    """
    Authorization request DTO.
    """

    username: str
    password: str
