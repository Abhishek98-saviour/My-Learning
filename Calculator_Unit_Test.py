# test_calculator.py
import unittest
from Calculator import calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a new calculator instance for each test"""
        self.calc = calculator()

    def test_add(self):
        """Test addition"""
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        """Test subtraction"""
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply(self):
        """Test multiplication"""
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """Test division"""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(1, 2), 0.5)

        # Test divide by zero
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

if __name__ == '__main__':
    # Create a test suite and add test cases
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCalculator))

    # Set up a test runner with detailed output
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity=2 for more detailed output
    runner.run(suite)