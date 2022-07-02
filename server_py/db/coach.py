import sqlalchemy
from .base import metadata

coaches = sqlalchemy.Table(
    'coaches',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
)