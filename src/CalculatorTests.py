import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):


    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator,Calculator)

    def test_calculator_addition(self):
        calculator = Calculator()
        result = calculator.addition(91, 143)
        self.assertEqual(234, result)

    def test_calculator_subrtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(972, 425)
        self.assertEqual(547, result)

    def test_calculator_multiplication(self):
        calculator = Calculator()
        result = calculator.multiplication(499, 109)
        self.assertEqual(54391, result)

    def test_calculator_squareroot(self):
        calculator = Calculator()
        result = calculator.division(4], 2)
        self.assertEqual(2, result)

    def test_calculator_square(self):
        calculator = Calculator()
        result = calculator.square(78)
        self.assertEqual(6084, result)

    def test_calculator_squareroot(self):
        calculator = Calculator()
        result = calculator.squareroot(17)
        self.assertEqual(4.123106, result)

    def test_calculator_addition(self):
        calculator = Calculator()
        result = calculator.addition(49, 359)
        self.assertEqual(408, result)





if __name__ == '__main__':
    unittest.main()
