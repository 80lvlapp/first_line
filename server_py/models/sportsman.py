from pydantic import BaseModel
from datetime import date
from enums.sex_enum import Sex


class SportsmanModel(BaseModel):
    id: int
    name: str
    # date_birth: date
    #sex: Sex


class SportsmanModelIn(BaseModel):
    name: str
    # date_birth: date
    #sex: Sex
