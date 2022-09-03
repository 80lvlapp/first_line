from pydantic import BaseModel


class TournamentModelDisplay1(BaseModel):
    id: int
    name: str
    venue: str

    class Config():
        orm_mode = True


class TypeOfTournamentsModel(BaseModel):
    id: int
    name: str


class TypeTournamentsModelDisplay(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True


class TypeOfTournamentsModelIn(BaseModel):
    id: int
    name: str
    tournament: list[TournamentModelDisplay1] = []

    class Config():
        orm_mode = True
