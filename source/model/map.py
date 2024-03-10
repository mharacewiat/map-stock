from pydantic import BaseModel


class Map(BaseModel):
    
    id: str
    file_path: str = ""
    is_processed: int = 0
    is_public: int = 1
