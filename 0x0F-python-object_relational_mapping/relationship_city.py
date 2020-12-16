#!/usr/bin/python3
'''
Improve the files model_city.py and model_state.py, and save them as
relationship_city.py and relationship_state.py
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    '''
    Improve the files model_city.py and model_state.py, and save them as
    relationship_city.py and relationship_state.py
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
