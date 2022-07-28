from pydantic import BaseModel



class TournamentModel(BaseModel):
    id: int
    id_type_of_tournament: int
    name: str
    venue: str


class TournamentModelIn(BaseModel):
    id_type_of_tournament: int
    name: str
    venue: str
