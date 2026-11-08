import unittest
from app import add, subtract, multi, divide

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multi(self):
        self.assertEqual(multi(5, 3), 15)
        self.assertEqual(multi(-1, 1), -1)
        self.assertEqual(multi(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(-6, -3), 2)
        with self.assertRaises(ZeroDivisionError):
            divide(6, 0)
            
if __name__ == '__main__':
    unittest.main()