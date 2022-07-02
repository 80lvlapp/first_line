from .base import BaseRepository
from models.school_model import SchoolModel, SchoolModelIn
from typing import List, Optional
from db.school import schools


class SchoolRepository(BaseRepository):

    async def create(self, param: SchoolModelIn) -> SchoolModel:
        element = SchoolModel(
            id=0,
            name=param.name,
            address=param.address
        )
        values = {**param.dict()}
        values.pop("id", None)
        query = schools.insert().values(**values)
        element.id = await  self.database.execute(query=query)
        return element

    async def update(self, id: int, param: SchoolModelIn) -> SchoolModel:
        element = SchoolModel(
            id=id,
            name=param.name,
            address=param.address
        )
        values = {**element.dict()}
        values.pop("id", None)
        query = schools.update().where(schools.c.id == id).values(**values)
        await self.database.execute(query=query)
        return element

    async def delete(self, id: int):
        query = schools.delete().where(schools.c.id == id)
        return await self.database.execute(query=query)

    async def get_all(self) -> List[SchoolModel]:
        query = schools.select()
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[SchoolModel]:
        query = schools.select().where(schools.c.id == id)
        element = await  self.database.fetch_one(query=query)
        if element is None:
            return None
        return SchoolModel.parse_obj(element)
