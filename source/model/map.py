from pydantic import BaseModel


class Map(BaseModel):
    
    id: str
    path: str
