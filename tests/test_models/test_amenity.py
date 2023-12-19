#!/usr/bin/python3
""" """
import os
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel


class test_Amenity(test_basemodel):
    """ It tests class"""

    def __init__(self, *args, **kwargs):
        """It test class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """It is testing name type """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
