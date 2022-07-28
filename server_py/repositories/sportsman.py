import enums.sex_enum
from .base import BaseRepository
from schemas.sportsman import SportsmanModel, SportsmanModelIn
from typing import List, Optional
from db.sportsman import sportsman
from datetime import timezone


class Repository(BaseRepository):

    async def create(self, param: SportsmanModelIn) -> SportsmanModel:
        element = SportsmanModel(
            id=0,
            name=param.name,
            # date_birth=timezone.fromutc(param.date_birth).date(),
            # sex=param.sex == "Male" if enums.sex_enum.Sex.male else enums.sex_enum.Sex.female
        )
        values = {**param.dict()}
        values.pop("id", None)
        query = sportsman.insert().values(**values)
        element.id = await  self.database.execute(query=query)
        return element

    async def update(self, id: int, param: SportsmanModelIn) -> SportsmanModel:
        element = SportsmanModel(
            id=id,
            name=param.name,
            # date_birth=timezone.fromutc(param.date_birth).date(),
            # sex=param.sex == "Male" if enums.sex_enum.Sex.male else enums.sex_enum.Sex.female
        )
        values = {**element.dict()}
        values.pop("id", None)
        query = sportsman.update().where(sportsman.c.id == id).values(**values)
        await self.database.execute(query=query)
        return element

    async def delete(self, id: int):
        query = sportsman.delete().where(sportsman.c.id == id)
        return await self.database.execute(query=query)

    async def get_all(self) -> List[SportsmanModel]:
        query = sportsman.select()
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[SportsmanModel]:
        query = sportsman.select().where(sportsman.c.id == id)
        element = await  self.database.fetch_one(query=query)
        if element is None:
            return None
        return SportsmanModel.parse_obj(element)
