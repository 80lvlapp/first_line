from .base import BaseRepository
from schemas.tournament_model import TournamentModel, TournamentModelIn

from typing import List, Optional
from db.value_categories import value_categories



class TournamentRepository(BaseRepository):

    async def create(self, param: TournamentModelIn) -> TournamentModel:
        element = TournamentModel(
            id=0,
            category_id=param.category_id,
            name=param.name,
        )
        values = {**param.dict()}
        values.pop("id", None)
        query = value_categories.insert().values(**values)
        element.id = await  self.database.execute(query=query)
        return element

    async def update(self, id: int, param: TournamentModelIn) -> TournamentModel:
        element = TournamentModel(
            id=id,
            category_id=param.category_id,
            name=param.name,
        )
        values = {**element.dict()}
        values.pop("id", None)
        query = value_categories.update().where(value_categories.c.id == id).values(**values)
        await self.database.execute(query=query)
        return element

    async def delete(self, id: int):
        query = value_categories.delete().where(value_categories.c.id == id)
        return await self.database.execute(query=query)

    async def get_all(self) -> List[TournamentModel]:
        query = value_categories.select()
        return await self.database.fetch_all(query=query)


    async def get_by_id(self, id: int) -> Optional[TournamentModel]:
        query = value_categories.select().where(value_categories.c.id == id)
        element = await self.database.fetch_one(query=query)
        if element is None:
            return None
        return TournamentModel.parse_obj(element)
