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

from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """State class/table model."""
    __tablename__ = 'states'
    
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """Returns the list of City instances with state_id
            equal to the current State.id.
            This mimics the FileStorage relationship between State and City.
            """
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
