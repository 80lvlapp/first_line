

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models.school_model import SchoolModel, SchoolModelIn
from .depends import getSchoolRepository
from repositories.school_repository import SchoolRepository

router = APIRouter()


@router.get("/", response_model=List[SchoolModel], status_code=200)
async def get_all(repository: SchoolRepository = Depends(getSchoolRepository)):
    return await repository.get_all()


@router.get("/{id}", response_model=SchoolModel)
async def get_by_id(id: int, repository: SchoolRepository = Depends(getSchoolRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return element


@router.post("/", response_model=SchoolModel, status_code=201)
async def create(param: SchoolModelIn,
                 repository: SchoolRepository = Depends(getSchoolRepository)):
    return await repository.create(param=param)


@router.put("/{id}", response_model=SchoolModel, status_code=201)
async def update(
        id: int,
        param: SchoolModelIn,
        repository: SchoolRepository = Depends(getSchoolRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return await repository.update(id=id, param=param)


@router.delete("/{id}")
async def delete(id: int, repository: SchoolRepository = Depends(getSchoolRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    await repository.delete(id=id)
    return {"status": True}
