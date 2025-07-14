import os
import sqlmodel
from sqlmodel import Session, SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL == "":
    raise NotImplementedError("'DATABASE_URL' was not set")

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print('Creating all tables...')
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

