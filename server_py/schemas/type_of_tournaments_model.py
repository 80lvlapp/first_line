from pydantic import BaseModel


class TypeOfTournamentsModel(BaseModel):
    id: int
    name: str


class TypeOfTournamentsModelIn(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True
