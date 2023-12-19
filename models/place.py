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

from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship

if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )

class Place(BaseModel, Base):
    """A place to stay."""
    __tablename__ = 'places'
    
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns the list of Review instances with place_id
            equal to the current Place.id.
            This mimics the FileStorage relationship between Place and Review.
            """
            from models import storage
            all_revs = storage.all(Review)
            lst = []
            for rev in all_revs.values():
                if rev.place_id == self.id:
                    lst.append(rev)
            return lst

        @property
        def amenities(self):
            """Returns the list of Amenity instances
            based on the attribute amenity_ids that
            contains all Amenity.id linked to the Place.
            This mimics the FileStorage relationship between Place and Amenity.
            """
            from models import storage
            all_amens = storage.all(Amenity)
            lst = []
            for amen in all_amens.values():
                if amen.id in self.amenity_ids:
                    lst.append(amen)
            return lst

        @amenities.setter
        def amenities(self, obj):
            """Method for adding an Amenity.id to the
            attribute amenity_ids. Accepts only Amenity
            objects.
            """
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
