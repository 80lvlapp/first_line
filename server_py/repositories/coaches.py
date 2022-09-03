from sqlalchemy.orm.session import Session
from db.models import CoachDb
from schemas.coach import CoachModel, CoachModeDisplay


def create(db: Session, request: CoachModel):
    element = CoachDb(
        name=request.name
    )
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def get_all_elements(db: Session) -> list[CoachModeDisplay]:
    return db.query(CoachDb).all()


def get_element_by_id(id: int, db: Session) -> CoachModeDisplay:
    return db.query(CoachDb).filter(CoachDb.id == id).first()


def update_element(id: int, request: CoachModeDisplay, db: Session) -> CoachModeDisplay:
    element = db.query(CoachDb).get(id)
    element.name = request.name
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def delete_element(id: int, db: Session) -> None:
    element = db.query(CoachDb).get(id)
    db.delete(element)
    db.commit()
