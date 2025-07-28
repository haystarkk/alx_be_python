import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        

    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(2, 3), 6)      # positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # negative × positive
        self.assertEqual(self.calc.multiply(-2, -3), 6)    # negative × negative
        self.assertEqual(self.calc.multiply(0, 100), 0)    # multiplication by zero

    def test_divide(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)       # normal division
        self.assertEqual(self.calc.divide(-9, 3), -3)      # negative ÷ positive
        self.assertEqual(self.calc.divide(5, 2), 2.5)      # division with float result
        self.assertIsNone(self.calc.divide(10, 0))         # division by zero should return None

        # Check division by zero returns None
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == '__main__':
    unittest.main()
