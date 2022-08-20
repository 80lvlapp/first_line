from sqlalchemy.orm.session import Session
from schemas.tournament_model import TournamentModelIn, TournamentModelDisplay
from db.models import TournamentsDb


def create(db: Session, request: TournamentModelIn) -> TournamentModelDisplay:
    element = TournamentsDb(
        name=request.name,
        id_type_tournament=request.id_type_tournament,
        venue=request.venue
    )
    db.add(element)
    db.commit()
    db.refresh(element)
    return element


def get_all_elements(db: Session) -> list[TournamentModelDisplay]:
    return db.query(TournamentsDb).all()


# def get_element_by_id(id: int, db: Session) -> TypeOfTournamentsModelIn:
#     return db.query(TournamentsDb).filter(TournamentsDb.id == id).first()
#
#
# def update_element(id: int, request: TypeOfTournamentsModelIn, db: Session) -> TypeOfTournamentsModelIn:
#     element = db.query(TournamentsDb).get(id)
#     element.name = request.name
#     db.add(element)
#     db.commit()
#     db.refresh(element)
#     return element
#
#
# def delete_element(id: int, db: Session) -> None:
#     element = db.query(TournamentsDb).get(id)
#     db.delete(element)
#     db.commit()
