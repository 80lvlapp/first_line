from pydantic import BaseModel
from schemas.type_tournaments import TypeOfTournamentsModel


class TournamentModel(BaseModel):
    id: int
    id_type_tournament: int
    name: str
    venue: str


class TournamentModelIn(BaseModel):
    id: int
    id_type_tournament: int
    name: str
    venue: str

    class Config:
        orm_mode = True


class TournamentModelDisplay(BaseModel):
    id: int
    name: str
    venue: str
    type_tournament: TypeOfTournamentsModel

    class Config():
        orm_mode = True
