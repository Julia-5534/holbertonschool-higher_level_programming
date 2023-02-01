#!/usr/bin/python3
"""unit tests for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRect(unittest.TestCase):
    """unit tests for Rectangle"""

    def test_base(self):
        self.assertIsInstance(Rectangle(2, 2), Base)

    def test_min_args(self):
        value = Rectangle(2, 2)
        self.assertEqual(value.area(), 4)

    def test_arg_limit(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 2, 2, 2)

    def test_privacy_1(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__width)

    def test_update_1(self):
        value = Rectangle(1, 1, 1, 1, 1)
        value.update(2)
        self.assertEqual(value.id, 2)
