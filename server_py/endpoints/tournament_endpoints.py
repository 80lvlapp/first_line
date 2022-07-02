from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models.tournament_model import TournamentModel, TournamentModelIn
from .depends import getTournamentRepository
from repositories.tournament_repository import TournamentRepository

router = APIRouter()


@router.get("/", response_model=List[TournamentModel], status_code=200)
async def get_all(repository: TournamentRepository = Depends(getTournamentRepository)):
    return await repository.get_all()


@router.get("/{id}", response_model=TournamentModel)
async def get_by_id(id: int, repository: TournamentRepository = Depends(getTournamentRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return element


@router.post("/", response_model=TournamentModel, status_code=201)
async def create(param: TournamentModelIn,
                 repository: TournamentRepository = Depends(getTournamentRepository)):
    return await repository.create(param=param)


@router.put("/{id}", response_model=TournamentModel, status_code=201)
async def update(
        id: int,
        param: TournamentModelIn,
        repository: TournamentRepository = Depends(getTournamentRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return await repository.update(id=id, param=param)


@router.delete("/{id}")
async def delete(id: int, repository: TournamentRepository = Depends(getTournamentRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    await repository.delete(id=id)
    return {"status": True}
