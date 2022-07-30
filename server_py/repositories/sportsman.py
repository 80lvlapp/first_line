from sqlalchemy.orm.session import Session
from db.models import SportsmanDb
from schemas.sportsman import SportsmanModelDisplay


def create(db: Session, request: SportsmanModelDisplay):
    element = SportsmanDb(
        name=request.name,
        date_birth=request.date_birth,
        sex=request.sex
    )
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def get_all_elements(db: Session) -> list[SportsmanModelDisplay]:
    return db.query(SportsmanDb).all()


def get_element_by_id(id: int, db: Session) -> SportsmanModelDisplay:
    return db.query(SportsmanDb).filter(SportsmanDb.id == id).first()


def update_element(id: int, request: SportsmanModelDisplay, db: Session) -> SportsmanModelDisplay:
    element = db.query(SportsmanDb).get(id)
    element.name = request.name
    element.date_birth = request.date_birth
    element.sex = request.sex
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def delete_element(id: int, db: Session) -> None:
    element = db.query(SportsmanDb).get(id)
    db.delete(element)
    db.commit()
