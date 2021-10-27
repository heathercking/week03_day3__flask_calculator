import unittest
from modules import calculator

class TestCalc(unittest.TestCase):

    def test_calaculator_can_add(self):
        assert calculator.add(1, 2) == 3

    def test_calaculator_can_subtract(self):
        assert calculator.subtract(3, 1) == 2

    def test_calaculator_can_multiply(self):
        assert calculator.multiply(2, 2) == 4

    def test_calaculator_can_divide(self):
        assert calculator.divide(4, 2) == 2


