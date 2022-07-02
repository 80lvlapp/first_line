import sqlalchemy
from .base import metadata

schools = sqlalchemy.Table(
    'schools',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column('address', sqlalchemy.String(100), nullable=True),
)