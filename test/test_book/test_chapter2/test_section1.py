from unittest import TestCase

from hamcrest import assert_that, is_
from hypothesis import given
from hypothesis.strategies import lists, integers

from array_util import create_array, is_sorted, is_permutation
from book.chapter2.section1 import insertion_sort, sum_array


class TestInsertionSort(TestCase):

    @given(lists(integers(), min_size=1))
    def test_insertion_sort(self, elements):
        A = create_array(elements)
        n = len(elements)

        insertion_sort(A, n)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))


class TestSumArray(TestCase):

    @given(lists(integers(), min_size=1))
    def test_sum_array(self, elements):
        A = create_array(elements)
        n = len(elements)

        actual_sum = sum_array(A, n)

        expected_sum = sum(elements)
        assert_that(actual_sum, is_(expected_sum))
