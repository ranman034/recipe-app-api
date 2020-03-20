"""Tests file"""
from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):
    """Example tests for calc"""
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_substract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
