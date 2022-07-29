from sqlalchemy.orm.session import Session
from schemas.categories import CategoriesModel
from db.models import CategoriesDb
from schemas.categories import CategoriesModeDisplay


def create(db: Session, request: CategoriesModel):
    element = CategoriesDb(
        name=request.name
    )
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def get_all_elements(db: Session) -> list[CategoriesModeDisplay]:
    return db.query(CategoriesDb).all()


def get_element_by_id(id: int, db: Session) -> CategoriesModeDisplay:
    return db.query(CategoriesDb).filter(CategoriesDb.id == id).first()
