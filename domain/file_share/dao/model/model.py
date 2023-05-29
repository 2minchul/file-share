from sqlalchemy import Column, Integer, String

from infra.db.sqlite_db import Base


class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)


class Link(Base):
    __tablename__ = 'link'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    path = Column(String, index=True)
    file_id = Column(Integer, index=True)
    download_count = Column(Integer, nullable=False, default=0)
