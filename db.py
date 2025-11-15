from databases import Database
from sqlalchemy import (MetaData, Table, Column, Integer, String, create_engine)
DATABASE_URL = 'sqlite:///./conocer.db'
database = Database(DATABASE_URL)
metadata = MetaData()
courses = Table(
    'courses', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('description', String, nullable=False)
)
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
