#!/usr/bin/python3
""" """
from models.place import Place
from tests.test_models.test_base_model import test_basemodel
import os


class test_Place(test_basemodel):
    """ It is a place tests class"""

    def __init__(self, *args, **kwargs):
        """ init test class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ It test place city_id attr"""
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """ It test place user_id attr"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """ It test place name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_description(self):
        """ it is testin place description attr"""
        new = self.value()
        self.assertEqual(type(new.description), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_rooms(self):
        """ it is testing place number of rooms attr"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_bathrooms(self):
        """ It is testing place number of bathrooms attr"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_max_guest(self):
        """ It is testing place max_guest attr"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_price_by_night(self):
        """ It test place price by night attr"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_latitude(self):
        """ It test place latitud attr"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_longitude(self):
        """ It test place longitude attr"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_amenity_ids(self):
        """ It test amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
