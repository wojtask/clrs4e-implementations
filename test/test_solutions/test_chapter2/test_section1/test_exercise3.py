import operator
from unittest import TestCase

from hamcrest import assert_that
from hypothesis import given
from hypothesis.strategies import lists, integers

from array_util import create_array, is_sorted, is_permutation
from solutions.chapter2.section1.exercise3 import insertion_sort_decreasing


class TestInsertionSortDecreasing(TestCase):

    @given(lists(integers(), min_size=1))
    def test_insertion_sort_decreasing(self, elements):
        A = create_array(elements)
        n = len(elements)

        insertion_sort_decreasing(A, n)

        assert_that(is_sorted(A, end=n, cmp=operator.ge))
        assert_that(is_permutation(A, elements, end=n))
