from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
#from schemas import UserBase
from db.database import get_db
#from db import db_user
#from schemas import UserDisplay


router = APIRouter(prefix="/api/categories", tags=["categories"])

