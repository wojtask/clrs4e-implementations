from unittest import TestCase

from hamcrest import *

from book.data_structures import Array
from solutions.chapter2.section3.exercise6 import binary_search


class TestBinarySearch(TestCase):

    def test_binary_search_positive(self):
        array = Array(1, 6)
        array[1] = 26
        array[2] = 31
        array[3] = 41
        array[4] = 41
        array[5] = 58
        array[6] = 59

        actual_index = binary_search(array, 1, 6, 58)

        assert_that(actual_index, is_(5))

    def test_binary_search_negative(self):
        array = Array(1, 6)
        array[1] = 26
        array[2] = 31
        array[3] = 41
        array[4] = 41
        array[5] = 58
        array[6] = 59

        actual_index = binary_search(array, 1, 6, 40)

        assert_that(actual_index, is_(None))
