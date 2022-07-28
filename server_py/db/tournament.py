import sqlalchemy
from .base1 import metadata
from .type_of_tournaments import type_of_tournaments

tournament = sqlalchemy.Table(
    'tournaments',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("id_type_of_tournament", sqlalchemy.ForeignKey(type_of_tournaments.c.id), nullable=False),
    sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
    #sqlalchemy.Column('date', sqlalchemy.Date, nullable=True),
    sqlalchemy.Column('venue', sqlalchemy.String(50), nullable=True),
)
