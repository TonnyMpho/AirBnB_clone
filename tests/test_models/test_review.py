#!/usr/bin/python3
"""Uniitest for class review"""
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test for the review class """
    def setUp(self):
        self.review = Review()

    def test_instance_creation(self):
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertEqual(type(self.review.id), str)

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_str_representation(self):
        expected_str = "[{}] ({}) {}".format(
            self.review.__class__.__name__,
            self.review.id,
            self.review.__dict__
        )
        self.assertEqual(str(self.review), expected_str)

    def test_args_unused(self):
        review = Review(None)
        self.assertNotIn(None, Review.__dict__.values())


if __name__ == '__main__':
    unittest.main()
