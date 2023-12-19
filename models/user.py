#!/usr/bin/python3
"""
This module defines a class User, representing a user with various attributes.
In a database-driven environment, it uses SQLAlchemy to map the User class to
the 'users' table. In a non-database environment, it defines attributes but
leaves them empty.
"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    This class defines a user with various attributes.

    Attributes:
        - email (str): User's email address.
        - password (str): User's password.
        - first_name (str): User's first name.
        - last_name (str): User's last name.

    In a database-driven environment (storage_type == 'db'):
        - It uses SQLAlchemy to map the User class to the 'users' table.
        - It includes columns for email, password, first_name, and last_name.
        - It establishes relationships with the Place and Review classes.
    In a non-database environment (storage_type != 'db'):
        - It defines attributes but leaves them empty.
    """
    __tablename__ = 'users'
    
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
