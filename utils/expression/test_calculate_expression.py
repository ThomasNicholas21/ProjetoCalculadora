import unittest
from utils.expression.calculate_expression import Calc


class TestCalc(unittest.TestCase):
    def test_calc_addition(self):
        self.assertEqual(Calc.evaluate("2 + 3"), 5)

    def test_calc_subtraction(self):
        self.assertEqual(Calc.evaluate("5 - 2"), 3)

    def test_calc_multiplication(self):
        self.assertEqual(Calc.evaluate("4 * 3"), 12)

    def test_calc_division(self):
        self.assertEqual(Calc.evaluate("10 / 2"), 5.0)

    def test_calc_combined_expression(self):
        self.assertEqual(Calc.evaluate("2 + 3 * 4"), 14)

    def test_calc_nested_operations(self):
        self.assertEqual(Calc.evaluate("(2 + 3) * 4"), 20)

    def test_calc_invalid_expression_raises(self):
        with self.assertRaises(KeyError):
            Calc.evaluate("2 ** 3")
