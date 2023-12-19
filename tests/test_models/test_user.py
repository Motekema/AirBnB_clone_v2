#!/usr/bin/python3
""" """
from models.user import User
from tests.test_models.test_base_model import test_basemodel
import os


class test_User(test_basemodel):
    """ It test class for user model"""

    def __init__(self, *args, **kwargs):
        """ Its a user test class init"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ It test user first anme attr"""
        new = self.value()
        self.assertEqual(type(new.first_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_last_name(self):
        """ its a testing 4 user last name attr"""
        new = self.value()
        self.assertEqual(type(new.last_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_email(self):
        """ its a testing 4 user email attr"""
        new = self.value()
        self.assertEqual(type(new.email), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_password(self):
        """ Its a testing 4 user password attr"""
        new = self.value()
        self.assertEqual(type(new.password), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
