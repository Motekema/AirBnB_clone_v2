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

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a city for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")

