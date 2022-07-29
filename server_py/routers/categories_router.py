from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.categories import CategoriesModeDisplay, CategoriesModel
from repositories import categories

from db.database import get_db

router = APIRouter(prefix="/api/categories", tags=["categories"])


# Create
@router.post("/", response_model=CategoriesModeDisplay)
async def create_element(request: CategoriesModel, db: Session = Depends(get_db)):
    element = categories.create(db=db, request=request)
    if element is None:
        raise HTTPException(status_code=400, detail="ERROR")
    return element
