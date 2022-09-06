from sqlalchemy import Boolean, Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import enum


class SexEnum(enum.Enum):
    male = "Male"
    female = "Female"


class CategoriesDb(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)


class CoachDb(Base):
    __tablename__ = "coaches"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)


class SchoolDb(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=True)


class SportsmanDb(Base):
    __tablename__ = "sportsmen"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)
    date_birth = Column(Date, nullable=True)
    sex = Column(Enum(SexEnum), default=SexEnum.male)


class TypeOfTournamentsDb(Base):
    __tablename__ = "type_of_tournaments"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)
    tournaments = relationship("TournamentsDb", back_populates="type_tournaments")


class TournamentsDb(Base):
    __tablename__ = "tournaments"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)
    venue = Column(String(50), nullable=True)
    id_type_tournament = Column(Integer, ForeignKey("type_of_tournaments.id"))
    type_tournaments = relationship("TypeOfTournamentsDb", back_populates="tournaments")
