from sqlalchemy.orm.session import Session
from schemas.categories import CategoriesModel
from db.models import CategoriesDb


def create(db: Session, request: CategoriesModel):
    element = CategoriesDb(
        name=request.name
    )
    db.add(element)
    db.commit()
    db.refresh(element)
    return element

# from schemas.categories import CategoriesModel, CategoriesModelIn
# from typing import List, Optional
# from db.categories import categories
#
#
# class CategoriesRepository(BaseRepository):
#
#     async def createCategory(self, param: CategoriesModelIn) -> CategoriesModel:
#         element = CategoriesModel(
#             id=0,
#             name=param.name
#         )
#         values = {**param.dict()}
#         values.pop("id", None)
#         query = categories.insert().values(**values)
#         element.id = await  self.database.execute(query=query)
#         return element
#
#     async def update(self, id: int, category: CategoriesModelIn) -> CategoriesModel:
#         element = CategoriesModel(
#             id=id,
#             name=category.name
#         )
#         values = {**element.dict()}
#         values.pop("id", None)
#         query = categories.update().where(categories.c.id == id).values(**values)
#         await self.database.execute(query=query)
#         return element
#
#     async def delete(self, id: int):
#         query = categories.delete().where(categories.c.id == id)
#         return await self.database.execute(query=query)
#
#     async def getAll(self) -> List[CategoriesModel]:
#         query = categories.select()
#         return await self.database.fetch_all(query=query)
#
#     async def getById(self, id: int) -> Optional[CategoriesModel]:
#         query = categories.select().where(categories.c.id == id)
#         element = await  self.database.fetch_one(query=query)
#         if element is None:
#             return None
#         return CategoriesModel.parse_obj(element)
