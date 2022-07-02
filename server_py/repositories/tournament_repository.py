from .base import BaseRepository
from models.tournament_model import TournamentModel, TournamentModelIn

from typing import List, Optional
from db.tournament import tournament
from db.type_of_tournaments import type_of_tournaments


class TournamentRepository(BaseRepository):

    async def create(self, param: TournamentModelIn) -> TournamentModel:
        element = TournamentModel(
            id=0,
            id_type_of_tournament=param.id_type_of_tournament,
            name=param.name,
            venue=param.venue
        )
        values = {**param.dict()}
        values.pop("id", None)
        query = tournament.insert().values(**values)
        element.id = await  self.database.execute(query=query)
        return element

    async def update(self, id: int, param: TournamentModelIn) -> TournamentModel:
        element = TournamentModel(
            id=id,
            id_type_of_tournament=param.id_type_of_tournament,
            name=param.name,
            venue=param.venue
        )
        values = {**element.dict()}
        values.pop("id", None)
        query = tournament.update().where(tournament.c.id == id).values(**values)
        await self.database.execute(query=query)
        return element

    async def delete(self, id: int):
        query = tournament.delete().where(tournament.c.id == id)
        return await self.database.execute(query=query)

    async def get_all(self) -> List[TournamentModel]:
        query = tournament.select()
        return await self.database.fetch_all(query=query)


    async def get_by_id(self, id: int) -> Optional[TournamentModel]:
        query = tournament.select().where(tournament.c.id == id)
        element = await  self.database.fetch_one(query=query)
        if element is None:
            return None
        return TournamentModel.parse_obj(element)
