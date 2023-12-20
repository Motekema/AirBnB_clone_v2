#!/usr/bin/python3
"""
Place Module for the HBNB project.

Defines the Place class to represent a place to stay. In a database-driven
environment, it uses SQLAlchemy to map the Place class to the 'places' table,
including columns for city_id, user_id, name, description, number_rooms,
number_bathrooms, max_guest, price_by_night, latitude, and longitude. It also
establishes relationships with the City, User, Review, and Amenity classes. In a
non-database environment, it defines attributes but leaves them empty.

Attributes:
    - city_id (str): The ID of the city associated with the place.
    - user_id (str): The ID of the user who owns the place.
    - name (str): The name of the place.
    - description (str): A description of the place.
    - number_rooms (int): The number of rooms in the place.
    - number_bathrooms (int): The number of bathrooms in the place.
    - max_guest (int): The maximum number of guests the place can accommodate.
    - price_by_night (int): The price per night for staying at the place.
    - latitude (float): The latitude coordinate of the place.
    - longitude (float): The longitude coordinate of the place.
    - reviews (relationship): A relationship with the Review class.
    - amenities (relationship): A relationship with the Amenity class.

In a database-driven environment (storage_type == 'db'):
    - It uses SQLAlchemy to map the Place class to the 'places' table.
    - It includes columns for city_id, user_id, name, description, number_rooms,
      number_bathrooms, max_guest, price_by_night, latitude, and longitude.
    - It establishes relationships with the City, User, Review, and Amenity
      classes.
    - It includes a relationship table 'place_amenity' for the many-to-many
      relationship between Place and Amenity.

In a non-database environment (storage_type != 'db'):
    - It defines attributes but leaves them empty.
    - It includes properties for 'reviews' and 'amenities' that mimic the
      FileStorage relationships between Place and Review, and Place and Amenity,
      respectively.
"""

import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Represents the Place for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table places.

    Attributes:
        __tablename__ (str): A name of the MySQL table to store places.
        city_id (sqlalchemy String): A place's city id.
        user_id (sqlalchemy String): A place's user id.
        name (sqlalchemy String): The name.
        description (sqlalchemy String): The description.
        number_rooms (sqlalchemy Integer): The number of rooms.
        number_bathrooms (sqlalchemy Integer): The number of bathrooms.
        max_guest (sqlalchemy Integer): The maximum number of guests.
        price_by_night (sqlalchemy Integer): The price by night.
        latitude (sqlalchemy Float): The place's latitude.
        longitude (sqlalchemy Float): A place's longitude.
        reviews (sqlalchemy relationship): The Place-Review relationship.
        amenities (sqlalchemy relationship): The Place-Amenity relationship.
        amenity_ids (list): An id list of all linked amenities.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

