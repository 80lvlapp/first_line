from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.tournament_model import TournamentModelIn, TournamentModelDisplay
from repositories import tournament_repository

from db.database import get_db

router = APIRouter(prefix="/api/tournaments", tags=["tournaments"])


# Create
@router.post("/", response_model=TournamentModelDisplay)
async def create_element(request: TournamentModelIn, db: Session = Depends(get_db)):
    element = tournament_repository.create(db=db, request=request)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element


@router.get("/", response_model=list[TournamentModelDisplay])
async def get_all_elements(db: Session = Depends(get_db)):
    elements_list = tournament_repository.get_all_elements(db=db)
    if elements_list is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return elements_list


# @router.get("/{id}", response_model=SportsmanModelDisplay)
# async def get_element_by_id(id: int, db: Session = Depends(get_db)):
#     element = sportsman.get_element_by_id(id=id, db=db)
#     if element is None:
#         raise HTTPException(status_code=400, detail="ERROR")
#     return element
#
#
# @router.put("/{id}", response_model=SportsmanModelDisplay)
# async def update_element(id: int, request: SportsmanModelDisplay, db: Session = Depends(get_db)):
#     element = sportsman.update_element(id=id, request=request, db=db)
#     if element is None:
#         raise HTTPException(status_code=400, detail="ERROR")
#     return element
#
#
# @router.delete("/{id}")
# async def delete_element(id: int, db: Session = Depends(get_db)):
#     sportsman.delete_element(id=id, db=db)
#     return {"ok"}
