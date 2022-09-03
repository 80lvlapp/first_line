from sqlalchemy.orm.session import Session
from db.models import SchoolDb
from schemas.school_model import SchoolModelDisplay


def create(db: Session, request: SchoolModelDisplay):
    element = SchoolDb(
        name=request.name,
        address=request.address
    )
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def get_all_elements(db: Session) -> list[SchoolModelDisplay]:
    return db.query(SchoolDb).all()


def get_element_by_id(id: int, db: Session) -> SchoolModelDisplay:
    return db.query(SchoolDb).filter(SchoolDb.id == id).first()


def update_element(id: int, request: SchoolModelDisplay, db: Session) -> SchoolModelDisplay:
    element = db.query(SchoolDb).get(id)
    element.name = request.name
    element.address = request.address
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def delete_element(id: int, db: Session) -> None:
    element = db.query(SchoolDb).get(id)
    db.delete(element)
    db.commit()
