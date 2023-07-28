from unittest import TestCase

from hamcrest import *

from book.data_structures import Array
from solutions.chapter2.section3.exercise5 import recursive_insertion_sort


class TestRecursiveInsertionSort(TestCase):

    def test_recursive_insertion_sort(self):
        array = Array(1, 6)
        array[1] = 5
        array[2] = 2
        array[3] = 4
        array[4] = 6
        array[5] = 1
        array[6] = 3

        recursive_insertion_sort(array, 6)

        assert_that(array[1], is_(1))
        assert_that(array[2], is_(2))
        assert_that(array[3], is_(3))
        assert_that(array[4], is_(4))
        assert_that(array[5], is_(5))
        assert_that(array[6], is_(6))
