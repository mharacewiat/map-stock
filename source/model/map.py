from pydantic import BaseModel, Field
from uuid import uuid4, UUID


class Map(BaseModel):
    """
    Map domain model.
    """

    id: UUID = Field(default_factory=uuid4)
    file_path: str = ""
    is_processed: int = 0
    is_public: int = 1
