#!/usr/bin/python3
""" It is State Module for HBNB project """
from sqlalchemy import Column, String
from models import storage_type
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
