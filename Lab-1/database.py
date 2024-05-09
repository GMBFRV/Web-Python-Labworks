from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


class Dictionary(Base):
    __tablename__ = "dictionary"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    pages = Column(Integer)
    author = Column(String)


class Authors(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    books = Column(Integer)
    rating = Column(Integer)


SessionLocal = sessionmaker(autoflush=False, bind=engine)
