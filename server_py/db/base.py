from databases import Database
from sqlalchemy import create_engine, MetaData
from os import environ

DB_USER = environ.get('DB_USER', 'postgres')
DB_PASSWORD = environ.get('DB_PASS', 'sa')
DB_HOST = environ.get('DB_HOST', 'localhost')
DB_NAME = environ.get('DB_NAME', 'test')
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)
