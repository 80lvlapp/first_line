from sqlalchemy import Boolean, Column, Integer, String, Date, Enum
from .database import Base
import enum


# class DBUser(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50), unique=True, index=True)
#     email = Column(String(50), unique=True, index=True)
#     hashed_pass = Column(String)
#     is_active = Column(Boolean, default=True)

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
    address = Column(String(100), nullable=True)
    date_birth = Column(Date, nullable=True)
    sex = Column(Enum(SexEnum), default=SexEnum.male)
