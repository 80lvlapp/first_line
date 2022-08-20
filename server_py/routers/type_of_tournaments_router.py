from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.type_tournaments import TypeOfTournamentsModelIn
from repositories import type_of_tournaments_repository

from db.database import get_db

router = APIRouter(prefix="/api/type-of-tournaments", tags=["type-of-tournaments"])


# Create
@router.post("/", response_model=TypeOfTournamentsModelIn)
async def create_element(request: TypeOfTournamentsModelIn, db: Session = Depends(get_db)):
    element = type_of_tournaments_repository.create(db=db, request=request)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.get("/", response_model=list[TypeOfTournamentsModelIn])
async def get_all_elements(db: Session = Depends(get_db)):
    elements_list = type_of_tournaments_repository.get_all_elements(db=db)
    if elements_list is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return elements_list


@router.get("/{id}", response_model=TypeOfTournamentsModelIn)
async def get_element_by_id(id: int, db: Session = Depends(get_db)):
    element = type_of_tournaments_repository.get_element_by_id(id=id, db=db)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.put("/{id}", response_model=TypeOfTournamentsModelIn)
async def update_element(id: int, request: TypeOfTournamentsModelIn, db: Session = Depends(get_db)):
    element = type_of_tournaments_repository.update_element(id=id, request=request, db=db)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.delete("/{id}")
async def delete_element(id: int, db: Session = Depends(get_db)):
    type_of_tournaments_repository.delete_element(id=id, db=db)
    return {"ok"}
