from .base import BaseRepository
from schemas.coach import CoachModel,  CoachModelIn
from typing import List, Optional
from db.coach import coaches


class Repository(BaseRepository):

    async def create(self, param: CoachModelIn) -> CoachModel:
        element = CoachModel(
            id=0,
            name=param.name
        )
        values = {**param.dict()}
        values.pop("id", None)
        query = coaches.insert().values(**values)
        element.id = await  self.database.execute(query=query)
        return element

    async def update(self, id: int, param: CoachModelIn) -> CoachModel:
        element = CoachModel(
            id=id,
            name=param.name
        )
        values = {**element.dict()}
        values.pop("id", None)
        query = coaches.update().where(coaches.c.id == id).values(**values)
        await self.database.execute(query=query)
        return element

    async def delete(self, id: int):
        query = coaches.delete().where(coaches.c.id == id)
        return await self.database.execute(query=query)

    async def get_all(self) -> List[CoachModel]:
        query = coaches.select()
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[CoachModel]:
        query = coaches.select().where(coaches.c.id == id)
        element = await  self.database.fetch_one(query=query)
        if element is None:
            return None
        return CoachModel.parse_obj(element)
