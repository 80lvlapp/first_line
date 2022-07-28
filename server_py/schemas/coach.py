from pydantic import BaseModel


class CoachModel(BaseModel):
    id: int
    name: str


class CoachModelIn(BaseModel):
    name: str
