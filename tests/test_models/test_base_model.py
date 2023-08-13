#!/usr/bin/python3
""" Unittest for BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Unittest """
    def setUp(self):
        """ Create an instance """
        self.base_model = BaseModel()

    def test_attributes(self):
        """Check if the class has the attributes """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        """ Check if the class id is a string """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """
        Check if the class created_at & updated at is a datetime instance
        """
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """ Check the class string representation"""
        str_representation = str(self.base_model)
        self.assertIn("[BaseModel]", str_representation)
        self.assertIn(str(self.base_model.id), str_representation)

    def test_save_method(self):
        """ test if it saves """
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """ check if it converts everything to dick """
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(base_model_dict['created_at']), str)
        self.assertEqual(type(base_model_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
