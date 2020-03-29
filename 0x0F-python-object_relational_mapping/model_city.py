#!/usr/bin/python3
"""
 Contains the class definition of a City
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ Representation of a city """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
