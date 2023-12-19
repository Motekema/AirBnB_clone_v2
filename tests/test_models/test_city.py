#!/usr/bin/python3
""" """
from models.city import City
from tests.test_models.test_base_model import test_basemodel
import os


class test_City(test_basemodel):
    """ It tests for city """

    def __init__(self, *args, **kwargs):
        """ Its a init test class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ It test state_id type """
        new = self.value()
        self.assertEqual(type(new.state_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """ It tests name type"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
