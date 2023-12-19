#!/usr/bin/python3
'''
Database storage engine for HBNB project.

Defines the DBStorage class, a database storage engine for MySQL storage.
Uses SQLAlchemy to interact with a MySQL database. Manages different
classes such as User, State, City, Amenity, Place, and Review.

Attributes:
    - __engine (SQLAlchemy Engine): The SQLAlchemy engine for database
      interaction.
    - __session (SQLAlchemy Session): The current SQLAlchemy session for
      database operations.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    '''
    Database storage engine for MySQL storage.

    Manages different classes such as User, State, City, Amenity, Place, and
    Review. Uses SQLAlchemy to interact with a MySQL database.
    '''

    __engine = None
    __session = None

    def __init__(self):
        '''
        Instantiate a new DBStorage instance.

        Creates the SQLAlchemy engine for MySQL interaction.
        '''
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB
            ), pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        Query on the current DB session all objects of a specific class.

        Args:
            - cls (class): The class to query. If None, queries all classes.

        Returns:
            Dictionary of queried objects with format "Classname.id": object.
        '''
        dct = {}
        if cls is None:
            for c in classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dct[key] = obj
        return dct

    def new(self, obj):
        '''
        Adds the object to the current DB session.

        Args:
            - obj (BaseModel): The object to add to the session.
        '''
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        '''Commit all changes of the current DB session.'''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Deletes the object from the current DB session, if it is not None.

        Args:
            - obj (BaseModel): The object to delete from the session.
        '''
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        '''Reloads the database.'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """Closes the working SQLAlchemy session."""
        self.__session.close()
