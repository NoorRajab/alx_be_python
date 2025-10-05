import unittest
# Assuming simple_calculator.py is in the same directory
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, covering all arithmetic operations.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator instance.
        """
        self.calc = SimpleCalculator()

    # ---------------------------
    # Test Cases for ADDITION
    # ---------------------------

    def test_addition(self):
        """Test addition with two positive integers."""
        self.assertEqual(self.calc.add(5, 7), 12)
        self.assertEqual(self.calc.add(100, 200), 300)
        """Test addition with two negative integers."""
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(-10, -5), -15)
        """Test addition with a mix of positive and negative integers."""
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(10, -5), 5)
        """Test addition with floating-point numbers."""
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3) # Use assertAlmostEqual for floats
        """Test addition when one operand is zero."""
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -10), -10)
        
    # ---------------------------
    # Test Cases for SUBTRACTION
    # ---------------------------

    def test_subtraction(self):
        """Test subtraction with positive integers."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(4, 10), -6)
        """Test subtraction with negative integers (e.g., -5 - (-2) = -3)."""
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        """Test subtraction involving mixed positive and negative numbers."""
        self.assertEqual(self.calc.subtract(10, -5), 15) # 10 - (-5) = 15
        self.assertEqual(self.calc.subtract(-10, 5), -15) # -10 - 5 = -15
        """Test subtraction when one operand is zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # ---------------------------
    # Test Cases for MULTIPLICATION
    # ---------------------------

    def test_multiply(self):
        """Test multiplication with two positive integers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(10, 10), 100)
        """Test multiplication involving negative integers."""
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        """Test multiplication when one operand is zero (critical edge case)."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-100, 0), 0)
        """Test multiplication involving floating-point numbers."""
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)
        
    # ---------------------------
    # Test Cases for DIVISION
    # ---------------------------

    def test_divide(self):
        """Test division of two positive integers resulting in a float."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        """Test division of zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)
        """
        Test the critical edge case: division by zero.
        The SimpleCalculator implementation returns None for this case.
        """
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

# Standard way to run the tests from within the file (though running via 
# 'python -m unittest' is the requested method)
if __name__ == '__main__':
    unittest.main()