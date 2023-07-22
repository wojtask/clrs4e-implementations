from unittest import TestCase

from hamcrest import *

from book.data_structures import Array
from solutions.chapter2.section1.exercise5 import add_binary_integers
from util import range_of


def bits_to_number(bits, n):
    result = 0
    for i in range_of(0, to=n - 1):
        result += bits[i] * 2 ** i
    return result


class TestAddBinaryIntegers(TestCase):

    def test_add_binary_integers(self):
        n = 3
        A = Array(0, n - 1)
        A[0] = 1
        A[1] = 0
        A[2] = 1
        B = Array(0, n - 1)
        B[0] = 1
        B[1] = 0
        B[2] = 0
        a = bits_to_number(A, n)
        b = bits_to_number(B, n)

        C = add_binary_integers(A, B, n)

        c = bits_to_number(C, n + 1)
        assert_that(c, is_(a + b))
