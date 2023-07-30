from unittest import TestCase

from hamcrest import *

from book.data_structures import Array
from solutions.chapter2.problem4 import count_inversions


class TestCountInversions(TestCase):

    def test_count_inversions(self):
        array = Array(1, 5)
        array[1] = 2
        array[2] = 3
        array[3] = 8
        array[4] = 6
        array[5] = 1

        actual_inversions = count_inversions(array, 1, 5)

        assert_that(actual_inversions, is_(5))
