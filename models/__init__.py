#!/usr/bin/python3
"""Instantiates a storage object.

-> The environmental variables 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storages engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

def create_storage():
    if getenv("HBNB_TYPE_STORAGE") == "db":
        return DBStorage()
    else:
        return FileStorage()

storage = create_storage()

