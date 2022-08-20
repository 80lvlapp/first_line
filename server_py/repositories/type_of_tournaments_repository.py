from sqlalchemy.orm.session import Session
from schemas.type_tournaments import TypeOfTournamentsModelIn
from db.models import TypeOfTournamentsDb


def create(db: Session, request: TypeOfTournamentsModelIn):
    element = TypeOfTournamentsDb(
        name=request.name
    )
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def get_all_elements(db: Session) -> list[TypeOfTournamentsModelIn]:
    return db.query(TypeOfTournamentsDb).all()


def get_element_by_id(id: int, db: Session) -> TypeOfTournamentsModelIn:
    return db.query(TypeOfTournamentsDb).filter(TypeOfTournamentsDb.id == id).first()


def update_element(id: int, request: TypeOfTournamentsModelIn, db: Session) -> TypeOfTournamentsModelIn:
    element = db.query(TypeOfTournamentsDb).get(id)
    element.name = request.name
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def delete_element(id: int, db: Session) -> None:
    element = db.query(TypeOfTournamentsDb).get(id)
    db.delete(element)
    db.commit()
