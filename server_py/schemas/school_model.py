from pydantic import BaseModel


class SchoolModel(BaseModel):
    id: int
    name: str
    address: str


class SchoolModelDisplay(BaseModel):
    id: int
    name: str
    address: str

    class Config():
        orm_mode = True
