from pydantic import BaseModel
from .type_of_tournaments_model import TypeOfTournamentsModel


class TournamentModel(BaseModel):
    id: int
    id_type_of_tournament: int
    name: str
    venue: str


class TournamentModelIn(BaseModel):
    id_type_of_tournament: int
    name: str
    venue: str
