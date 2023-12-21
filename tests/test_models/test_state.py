#!/usr/bin/python3
"""Testing save method """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Testing save method """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        ""Testing save method" """
        new = self.value()
        self.assertEqual(type(new.name), str)
