from repositories.categories import CategoriesRepository
from repositories.coaches import Repository as CoachesRepository
from repositories.sportsman import Repository as SportsmanRepository
from repositories.school_repository import SchoolRepository
from repositories.type_of_tournaments_repository import TypeOfTournamentsRepository
from repositories.tournament_repository import TournamentRepository
from db.base import database


def getCategoriesRepository() -> CategoriesRepository:
    return CategoriesRepository(database)


def getCoachesRepository() -> CoachesRepository:
    return CoachesRepository(database)


def getSportsmanRepository() -> SportsmanRepository:
    return SportsmanRepository(database)


def getSchoolRepository() -> SchoolRepository:
    return SchoolRepository(database)


def getTypeOfTournamentsRepository() -> TypeOfTournamentsRepository:
    return TypeOfTournamentsRepository(database)


def getTournamentRepository() -> TournamentRepository:
    return TournamentRepository(database)
