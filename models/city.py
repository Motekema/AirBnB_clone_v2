#!/usr/bin/python3
"""
City Module for HBNB project.

Defines the City class to represent a city, containing a state ID and name.
In a database-driven environment, it uses SQLAlchemy to map the City class to
the 'cities' table, including columns for name and state_id. It also establishes
a relationship with the State class. In a non-database environment, it defines
attributes but leaves them empty.

Attributes:
    - name (str): The name of the city.
    - state_id (str): The ID of the state associated with the city.

In a database-driven environment (storage_type == 'db'):
    - It uses SQLAlchemy to map the City class to the 'cities' table.
    - It includes columns for name and state_id.
    - It establishes a relationship with the State class.

In a non-database environment (storage_type != 'db'):
    - It defines attributes but leaves them empty.
"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """The City class, containing state ID and name."""
    __tablename__ = 'cities'
    
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
