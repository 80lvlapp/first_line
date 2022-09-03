from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.coach import CoachModeDisplay
from repositories import coaches

from db.database import get_db

router = APIRouter(prefix="/api/coach", tags=["coaches"])


# Create
@router.post("/", response_model=CoachModeDisplay)
async def create_element(request: CoachModeDisplay, db: Session = Depends(get_db)):
    element = coaches.create(db=db, request=request)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.get("/", response_model=list[CoachModeDisplay])
async def get_all_elements(db: Session = Depends(get_db)):
    elements_list = coaches.get_all_elements(db=db)
    if elements_list is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return elements_list


@router.get("/{id}", response_model=CoachModeDisplay)
async def get_element_by_id(id: int, db: Session = Depends(get_db)):
    element = coaches.get_element_by_id(id=id, db=db)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.put("/{id}", response_model=CoachModeDisplay)
async def update_element(id: int, request: CoachModeDisplay, db: Session = Depends(get_db)):
    element = coaches.update_element(id=id, request=request, db=db)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.delete("/{id}")
async def delete_element(id: int, db: Session = Depends(get_db)):
    coaches.delete_element(id=id, db=db)
    return {"ok"}
