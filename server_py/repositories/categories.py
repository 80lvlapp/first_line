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


def update_element(id: int, request: CategoriesModeDisplay, db: Session) -> CategoriesModeDisplay:
    element = db.query(CategoriesDb).get(id)
    element.name = request.name
    db.add(element)
    db.commit()
    db.refresh(element)
    return element

def delete_element(id: int, db: Session)->None:
    element = db.query(CategoriesDb).get(id)
    db.delete(element)
    db.commit()
