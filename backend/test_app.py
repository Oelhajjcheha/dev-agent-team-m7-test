import unittest

from app import add, subtract


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


class TestSubtract(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 0), 0)

    def test_subtract_mixed_signs(self):
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(5, -3), 8)

    def test_subtract_result_zero(self):
        self.assertEqual(subtract(7, 7), 0)


if __name__ == "__main__":
    unittest.main()
