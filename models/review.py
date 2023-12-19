#!/usr/bin/python3
"""
Review Module for the HBNB project.

Defines the Review class to store review information. In a database-driven
environment, it uses SQLAlchemy to map the Review class to the 'reviews' table,
including columns for text, place_id, and user_id. In a non-database
environment, it defines attributes but leaves them empty.

Attributes:
    - text (str): The text content of the review.
    - place_id (str): The ID of the place associated with the review.
    - user_id (str): The ID of the user who wrote the review.

In a database-driven environment (storage_type == 'db'):
    - It uses SQLAlchemy to map the Review class to the 'reviews' table.
    - It includes columns for text, place_id, and user_id.
    - It establishes foreign key relationships with the Place and User classes.

In a non-database environment (storage_type != 'db'):
    - It defines attributes but leaves them empty.
"""

from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Review(BaseModel, Base):
    """Review class to store review information."""
    __tablename__ = 'reviews'
    
    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
