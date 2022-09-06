from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.school_model import SchoolModelDisplay
from repositories import school_repository

from db.database import get_db

router = APIRouter(prefix="/api/rest-schools", tags=["schools"])


# Create
@router.post("/", response_model=SchoolModelDisplay)
async def create_element(request: SchoolModelDisplay, db: Session = Depends(get_db)):
    element = school_repository.create(db=db, request=request)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.get("/", response_model=list[SchoolModelDisplay])
async def get_all_elements(db: Session = Depends(get_db)):
    elements_list = school_repository.get_all_elements(db=db)
    if elements_list is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return elements_list


@router.get("/{id}", response_model=SchoolModelDisplay)
async def get_element_by_id(id: int, db: Session = Depends(get_db)):
    element = school_repository.get_element_by_id(id=id, db=db)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.put("/{id}", response_model=SchoolModelDisplay)
async def update_element(id: int, request: SchoolModelDisplay, db: Session = Depends(get_db)):
    element = school_repository.update_element(id=id, request=request, db=db)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.delete("/{id}")
async def delete_element(id: int, db: Session = Depends(get_db)):
    school_repository.delete_element(id=id, db=db)
    return {"ok"}
