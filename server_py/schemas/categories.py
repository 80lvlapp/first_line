from pydantic import BaseModel


class CategoriesModel(BaseModel):
    id: int
    name: str


class CategoriesModeDisplay(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True
