from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__all__ = ['Base', 'Session', 'create_tables']

engine = create_engine('sqlite:///db.sqlite')

Base = declarative_base()

Session = sessionmaker(bind=engine)


def create_tables():
    Base.metadata.create_all(engine)
