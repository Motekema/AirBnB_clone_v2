#!/usr/bin/python3
""" It is State Module for HBNB project """
from sqlalchemy import Column, String
from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represent an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to a MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of a MySQL table to store Amenities.
        name (sqlalchemy String): A amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
