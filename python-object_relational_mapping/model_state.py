#!/usr/bin/python3
"""This script lists all the state objects from the
hbtn_0e_6_usa database"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class state"""
    _tablename_ = 'states'
    id = Column(Inteeger, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
