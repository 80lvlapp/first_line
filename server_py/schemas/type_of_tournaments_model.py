from pydantic import BaseModel


class TypeOfTournamentsModel(BaseModel):
    id: int
    name: str


class TypeOfTournamentsModelIn(BaseModel):
    name: str
