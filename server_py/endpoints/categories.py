from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models.categories import CategoriesModel, CategoriesModelIn
from repositories.categories import CategoriesRepository
from .depends import getCategoriesRepository
from repositories.categories import CategoriesRepository

router = APIRouter()


@router.get("/", response_model=List[CategoriesModel], status_code=200)
async def get_all(categories: CategoriesRepository = Depends(getCategoriesRepository)):
    return await categories.getAll()


@router.get("/{id}", response_model=CategoriesModel)
async def get_element_by_id(id: int, categories: CategoriesRepository = Depends(getCategoriesRepository)):
    element = await categories.getById(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return element


@router.post("/", response_model=CategoriesModel, status_code=201)
async def create(category: CategoriesModelIn,
                         categories: CategoriesRepository = Depends(getCategoriesRepository)):
    return await categories.createCategory(param=category)


@router.put("/{id}", response_model=CategoriesModel, status_code=201)
async def update(
        id: int,
        category: CategoriesModelIn,
        categories: CategoriesRepository = Depends(getCategoriesRepository)):
    element = await categories.getById(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return await categories.update(id=id, category=category)


@router.delete("/{id}")
async def delete(id: int, categories: CategoriesRepository = Depends(getCategoriesRepository)):
    element = await categories.getById(id=id)
    if element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    await categories.delete(id=id)
    return {"status": True}
