from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from schemas.coach import CoachModel, CoachModelIn
from .depends import getCoachesRepository
from repositories.coaches import Repository

router = APIRouter()


@router.get("/", response_model=List[CoachModel], status_code=200)
async def get_all(repository: Repository = Depends(getCoachesRepository)):
    return await repository.get_all()


@router.get("/{id}", response_model=CoachModel)
async def get_by_id(id: int, repository: Repository = Depends(getCoachesRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return element


@router.post("/", response_model=CoachModel, status_code=201)
async def create(param: CoachModelIn,
                 repository: Repository = Depends(getCoachesRepository)):
    return await repository.create(param=param)


@router.put("/{id}", response_model=CoachModel, status_code=201)
async def update(
        id: int,
        param: CoachModelIn,
        repository: Repository = Depends(getCoachesRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return await repository.update(id=id, param=param)


@router.delete("/{id}")
async def delete(id: int, repository: Repository = Depends(getCoachesRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    await repository.delete(id=id)
    return {"status": True}
