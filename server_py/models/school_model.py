from pydantic import BaseModel


class SchoolModel(BaseModel):
    id: int
    name: str
    address: str


class SchoolModelIn(BaseModel):
    name: str
    address: str
