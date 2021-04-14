import unittest
from modules.calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(5, 15)  
        self.assertEqual("The answer is 20", result)

    def test_subtract(self):
        result = subtract(30, 5)
        self.assertEqual("The answer is 25", result)

    def test_multiply(self):
        result = multiply(5, 5)
        self.assertEqual("The answer is 25", result)

    def test_divide(self):
        result = divide(25, 5)
        self.assertEqual("The answer is 5.0", result)