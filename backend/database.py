from pydantic import BaseModel

class Equipment(BaseModel):
    id: int
    type: str
    name: str
    description: str