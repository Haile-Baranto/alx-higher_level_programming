#!/usr/bin/python3
"""
Script defining a State class and creating an instance of
declarative base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        __tablename__ (str): The name of the table associated
        with the class.
        id (int): An auto-generated unique identifier for the state.
        name (str): The name of the state, with a maximum length of
        128 characters.

    Note:
        This class must be imported before calling Base.metadata.
        create_all(engine).
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
