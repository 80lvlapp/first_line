from pydantic import BaseModel
from datetime import date
from db.models import SexEnum


class SportsmanModel(BaseModel):
    id: int
    name: str
    date_birth: date
    sex: SexEnum


class SportsmanModelDisplay(BaseModel):
    id: int
    name: str
    date_birth: date
    sex: SexEnum

    class Config():
        orm_mode = True
