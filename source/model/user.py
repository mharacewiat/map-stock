from pydantic import BaseModel


class User(BaseModel):

    username: str
    password: str
    is_active: int = 1
