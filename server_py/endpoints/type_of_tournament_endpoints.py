from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models.type_of_tournaments_model import TypeOfTournamentsModel, TypeOfTournamentsModelIn
from .depends import getTypeOfTournamentsRepository
from repositories.type_of_tournaments_repository import TypeOfTournamentsRepository

router = APIRouter()


@router.get("/", response_model=List[TypeOfTournamentsModel], status_code=200)
async def get_all(repository: TypeOfTournamentsRepository = Depends(getTypeOfTournamentsRepository)):
    return await repository.get_all()


@router.get("/{id}", response_model=TypeOfTournamentsModel)
async def get_by_id(id: int, repository: TypeOfTournamentsRepository = Depends(getTypeOfTournamentsRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return element


@router.post("/", response_model=TypeOfTournamentsModel, status_code=201)
async def create(param: TypeOfTournamentsModelIn,
                 repository: TypeOfTournamentsRepository = Depends(getTypeOfTournamentsRepository)):
    return await repository.create(param=param)


@router.put("/{id}", response_model=TypeOfTournamentsModel, status_code=201)
async def update(
        id: int,
        param: TypeOfTournamentsModelIn,
        repository: TypeOfTournamentsRepository = Depends(getTypeOfTournamentsRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return await repository.update(id=id, param=param)


@router.delete("/{id}")
async def delete(id: int, repository: TypeOfTournamentsRepository = Depends(getTypeOfTournamentsRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    await repository.delete(id=id)
    return {"status": True}
