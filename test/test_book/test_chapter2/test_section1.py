from unittest import TestCase

from hamcrest import *

from book.chapter2.section1 import insertion_sort, sum_array
from book.data_structures import Array


class TestInsertionSort(TestCase):

    def test_insertion_sort(self):
        array = Array(1, 6)
        array[1] = 5
        array[2] = 2
        array[3] = 4
        array[4] = 6
        array[5] = 1
        array[6] = 3

        insertion_sort(array, 6)

        assert_that(array[1], is_(1))
        assert_that(array[2], is_(2))
        assert_that(array[3], is_(3))
        assert_that(array[4], is_(4))
        assert_that(array[5], is_(5))
        assert_that(array[6], is_(6))


class TestSumArray(TestCase):

    def test_sum_array(self):
        array = Array(1, 6)
        array[1] = 5
        array[2] = 2
        array[3] = 4
        array[4] = 6
        array[5] = 1
        array[6] = 3

        actual_sum = sum_array(array, 6)

        assert_that(actual_sum, is_(21))
