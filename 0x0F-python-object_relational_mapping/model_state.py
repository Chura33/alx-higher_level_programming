#!/usr/bin/python3
"""
This module creates the base class
maps the class to the table
maps the instances to the rows
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ This creates a class
        called state and maps
        it to the table states
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
