from pydantic import BaseModel


class CoachModel(BaseModel):
    id: int
    name: str


class CoachModeDisplay(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
