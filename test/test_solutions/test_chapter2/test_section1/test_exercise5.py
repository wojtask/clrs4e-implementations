from unittest import TestCase

from hamcrest import assert_that, is_
from hypothesis import given
from hypothesis.strategies import lists, integers, composite

from array_util import create_array
from solutions.chapter2.section1.exercise5 import add_binary_integers
from util import range_of


def binary_to_decimal(A, n):
    result = 0
    for i in range_of(0, to=n - 1):
        result += A[i] * 2 ** i
    return result


@composite
def operands_in_binary(draw):
    n = draw(integers(min_value=1, max_value=63))
    operand1 = draw(lists(integers(min_value=0, max_value=1), min_size=n, max_size=n))
    operand2 = draw(lists(integers(min_value=0, max_value=1), min_size=n, max_size=n))
    return operand1, operand2


class TestAddBinaryIntegers(TestCase):

    @given(operands_in_binary())
    def test_add_binary_integers(self, operands):
        A = create_array(operands[0], start=0)
        B = create_array(operands[1], start=0)
        n = len(operands[0])
        a = binary_to_decimal(A, n)
        b = binary_to_decimal(B, n)

        C = add_binary_integers(A, B, n)

        c = binary_to_decimal(C, n + 1)
        assert_that(c, is_(a + b))
