#!/usr/bin/python3
"""
State class definition with relationship to City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """State class that inherits from Base"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='save-update, merge, delete',
                          backref='state')
