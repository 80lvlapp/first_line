import sqlalchemy
from .base import metadata

products = sqlalchemy.Table(
    'products',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('title', sqlalchemy.String(100)),
    sqlalchemy.Column('quantity', sqlalchemy.Float),
)
