from unittest import TestCase

from hamcrest import *

from book.data_structures import Array
from solutions.chapter2.section1.exercise4 import linear_search


class TestLinearSearch(TestCase):

    def test_linear_search_positive(self):
        array = Array(1, 4)
        array[1] = 5
        array[2] = 2
        array[3] = 4
        array[4] = 6

        actual_index = linear_search(array, 4, array[3])

        assert_that(actual_index, is_(equal_to(3)))

    def test_linear_search_negative(self):
        array = Array(1, 4)
        array[1] = 5
        array[2] = 2
        array[3] = 4
        array[4] = 6

        actual_index = linear_search(array, 4, 1)

        assert_that(actual_index, is_(None))
