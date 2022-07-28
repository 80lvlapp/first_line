# ValueCategoriesModel

from pydantic import BaseModel


class ValueCategoriesModel(BaseModel):
    id: int
    category_id: int
    name: str


class ValueCategoriesModelIn(BaseModel):
    category_id: int
    name: str
