#!/usr/bin/python3
"""
This file contains a class which inherits from sqlalchemy
declarative_base, a typical used system provided by the SQL
Alchemy ORM inorder to define classes mapped to relational database
tables
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class City(Base):
    """City class is a table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
