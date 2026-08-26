"""Unit tests for backend/app.py."""

import unittest

from app import add, subtract


class TestArithmetic(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_subtract_with_zero(self):
        self.assertEqual(subtract(7, 0), 7)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)


if __name__ == "__main__":
    unittest.main()
