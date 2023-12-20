#!/usr/bin/python3
"""
State Module for HBNB project.

Defines the State class/table model. In a database-driven environment, it uses
SQLAlchemy to map the State class to the 'states' table, including a column
for the state's name and a relationship with the City class. In a
non-database environment, it defines attributes but leaves them empty.

Attributes:
    - name (str): The name of the state.

In a database-driven environment (storage_type == 'db'):
    - It uses SQLAlchemy to map the State class to the 'states' table.
    - It includes a column for the state's name.
    - It establishes a relationship with the City class.

In a non-database environment (storage_type != 'db'):
    - It defines attributes but leaves them empty.
    - It includes a property 'cities' that returns a list of City instances
      with state_id equal to the current State.id. This mimics the
      FileStorage relationship between State and City.
"""

import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents the state for a MySQL database.

    Inherits from SQLAlchemy Base and links to a MySQL table states.

    Attributes:
        __tablename__ (str): A name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): A State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all the related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
