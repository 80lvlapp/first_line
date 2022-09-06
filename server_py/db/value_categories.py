import sqlalchemy
from .base1 import metadata
from .categories import categories

value_categories = sqlalchemy.Table(
    'value_categories',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("category_id", sqlalchemy.ForeignKey(categories.c.id), nullable=False),
    sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
)