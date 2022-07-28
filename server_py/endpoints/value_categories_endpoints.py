from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from schemas.value_categories_model import ValueCategoriesModel, ValueCategoriesModelIn
from .depends import getValueCategoriesRepository
from repositories.value_categories_repository import ValueCategoriesRepository

router = APIRouter()


@router.get("/", response_model=List[ValueCategoriesModel], status_code=200)
async def get_all(repository: ValueCategoriesRepository = Depends(getValueCategoriesRepository)):
    return await repository.get_all()


@router.get("/{id}", response_model=ValueCategoriesModel)
async def get_by_id(id: int, repository: ValueCategoriesRepository = Depends(getValueCategoriesRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return element


@router.post("/", response_model=ValueCategoriesModel, status_code=201)
async def create(param: ValueCategoriesModelIn,
                 repository: ValueCategoriesRepository = Depends(getValueCategoriesRepository)):
    return await repository.create(param=param)


@router.put("/{id}", response_model=ValueCategoriesModel, status_code=201)
async def update(
        id: int,
        param: ValueCategoriesModelIn,
        repository: ValueCategoriesRepository = Depends(getValueCategoriesRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return await repository.update(id=id, param=param)


@router.delete("/{id}")
async def delete(id: int, repository: ValueCategoriesRepository = Depends(getValueCategoriesRepository)):
    element = await repository.get_by_id(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    await repository.delete(id=id)
    return {"status": True}
