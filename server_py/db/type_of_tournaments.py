import sqlalchemy
from .base import metadata

type_of_tournaments = sqlalchemy.Table(
    'type_of_tournaments',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
)