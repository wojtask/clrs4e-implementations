from unittest import TestCase

from hamcrest import *

from book.data_structures import Array
from solutions.chapter2.section3.exercise8 import sum_search


class TestSumSearch(TestCase):

    def test_sum_search_positive(self):
        array = Array(1, 6)
        array[1] = 26
        array[2] = 31
        array[3] = 41
        array[4] = 41
        array[5] = 58
        array[6] = 59

        actual_found = sum_search(array, 6, 90)

        assert_that(actual_found, is_(True))

    def test_sum_search_negative(self):
        array = Array(1, 6)
        array[1] = 26
        array[2] = 31
        array[3] = 41
        array[4] = 41
        array[5] = 58
        array[6] = 59

        actual_found = sum_search(array, 6, 91)

        assert_that(actual_found, is_(False))
