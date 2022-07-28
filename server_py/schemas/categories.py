from pydantic import BaseModel


class CategoriesModel(BaseModel):
    id: int
    name: str


class CategoriesModelIn(BaseModel):
    name: str

