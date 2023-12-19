#!/usr/bin/python3
""" """
from models.state import State
from tests.test_models.test_base_model import test_basemodel
import os


class test_state(test_basemodel):
    """ It is the states test class"""

    def __init__(self, *args, **kwargs):
        """ Its the state test class init"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ It is testing state name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
