#!/usr/bin/python3
""" Its the module for testing file storage"""
import unittest
from models import storage
from models.base_model import BaseModel
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'fileStorage test not supported')
class test_fileStorage(unittest.TestCase):
    """ It is a class to test file storage method """

    def setUp(self):
        """ It sets up tests environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ It removes storage file at end of the tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """ The __objects are initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ The new objects are correctly to __objects """
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ All __objects are properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ The iles are not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ It saves data to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ The fileStorage saves method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ The storage file is successfully loaded - __objects """
        new = BaseModel()
        new.save()
        storage.reload()
        loaded = None
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ It loads from empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Non happens if the file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ It saves method calls from storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ It confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ It confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Is the key is properly formatted """
        new = BaseModel()
        new.save()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ The fileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)
