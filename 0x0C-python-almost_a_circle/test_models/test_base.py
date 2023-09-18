#!/usr/bin/python3
"""Unit tests for the Base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_no_id(self):
        """Test that Base assigns unique IDs when no ID is provided"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_with_id(self):
        """Test that Base assigns the provided ID when one is given"""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_private_attribute(self):
        """Test that __nb_objects is a private class attribute"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)


if __name__ == '__main__':
    unittest.main()
