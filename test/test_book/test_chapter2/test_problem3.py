from unittest import TestCase

from hamcrest import *

from book.chapter2.problem3 import horner
from book.data_structures import Array


class TestHorner(TestCase):

    def test_horner(self):
        coefficients = Array(0, 3)
        coefficients[0] = 2.1
        coefficients[1] = -4
        coefficients[2] = 0
        coefficients[3] = 1.5
        x = 2

        actual_value = horner(coefficients, 3, x)

        expected_value = \
            coefficients[0] + \
            coefficients[1] * x + \
            coefficients[2] * x ** 2 + \
            coefficients[3] * x ** 3
        assert_that(actual_value, is_(expected_value))
