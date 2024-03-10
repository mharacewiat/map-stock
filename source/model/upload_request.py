from typing import Any
from pydantic import BaseModel
from typing_extensions import Annotated


class UploadRequestModel(BaseModel):
    """
    Upload request DTO.
    """

    file: Any
