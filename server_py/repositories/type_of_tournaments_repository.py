from .base import BaseRepository
from schemas.type_of_tournaments_model import TypeOfTournamentsModel, TypeOfTournamentsModelIn
from typing import List, Optional
from db.type_of_tournaments import type_of_tournaments


class TypeOfTournamentsRepository(BaseRepository):

    async def create(self, param: TypeOfTournamentsModelIn) -> TypeOfTournamentsModel:
        element = TypeOfTournamentsModel(
            id=0,
            name=param.name
        )
        values = {**param.dict()}
        values.pop("id", None)
        query = type_of_tournaments.insert().values(**values)
        element.id = await  self.database.execute(query=query)
        return element

    async def update(self, id: int, param: TypeOfTournamentsModelIn) -> TypeOfTournamentsModel:
        element = TypeOfTournamentsModel(
            id=id,
            name=param.name
        )
        values = {**element.dict()}
        values.pop("id", None)
        query = type_of_tournaments.update().where(type_of_tournaments.c.id == id).values(**values)
        await self.database.execute(query=query)
        return element

    async def delete(self, id: int):
        query = type_of_tournaments.delete().where(type_of_tournaments.c.id == id)
        return await self.database.execute(query=query)

    async def get_all(self) -> List[TypeOfTournamentsModel]:
        query = type_of_tournaments.select()
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[TypeOfTournamentsModel]:
        query = type_of_tournaments.select().where(type_of_tournaments.c.id == id)
        element = await  self.database.fetch_one(query=query)
        if element is None:
            return None
        return TypeOfTournamentsModel.parse_obj(element)
