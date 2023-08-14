#!/bin/usr/python3
""" Tests for the user module """
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """ Unittests """
    def setUp(self):
        self.user = User()

    def test_instance_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertEqual(type(self.user.id), str)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))


    def test_email(self):
        self.user.email = "airbnb@mail.com"
        self.assertEqual(self.user.email, "airbnb@mail.com")

    def test_password(self):
        self.user.password = "root"
        self.assertEqual(self.user.password, "root")

    def test_first_name(self):
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")

    def test_last_name(self):
        """Tests the last_name attribute of User class."""
        self.user.last_name = "Bar"
        self.assertEqual(self.user.last_name, "Bar")

    def test_str_representation(self):
        expected_str = "[{}] ({}) {}".format(
            self.user.__class__.__name__,
            self.user.id,
            self.user.__dict__
        )
        self.assertEqual(str(self.user), expected_str)


if __name__ == '__main__':
    unittest.main()
