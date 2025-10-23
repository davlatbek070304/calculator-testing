import unittest
from calculator_operations import add, sub, mul, div

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)

    def test_mul(self):
        self.assertEqual(mul(4, 5), 20)

    def test_div(self):
        self.assertEqual(div(8, 2), 4)

    def test_div_zero(self):
        with self.assertRaises(ValueError):
            div(5, 0)

if __name__ == "__main__":
    unittest.main()
