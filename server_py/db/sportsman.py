import enum

import sqlalchemy
from sqlalchemy import Enum
from enums.sex_enum import Sex

from .base import metadata

sportsman = sqlalchemy.Table(
    'sportsmen',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
    #sqlalchemy.Column("date_birth", sqlalchemy.Date, nullable=True),
    #sqlalchemy.Column("sex", sqlalchemy.Enum(Sex), default=Sex.male, nullable=False)
)
