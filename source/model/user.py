from pydantic import BaseModel


class User(BaseModel):
    """
    User domain model.
    """

    username: str
    password: str
    is_active: int = 1
