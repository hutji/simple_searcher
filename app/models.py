from sqlalchemy import ARRAY, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    rubrics = Column(ARRAY(String))
    text = Column(String)
    created_date = Column(DateTime)
