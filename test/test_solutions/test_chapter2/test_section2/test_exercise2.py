from unittest import TestCase

from hamcrest import assert_that
from hypothesis import given
from hypothesis.strategies import lists, integers

from array_util import create_array, is_sorted, is_permutation
from solutions.chapter2.section2.exercise2 import selection_sort


class TestSelectionSort(TestCase):

    @given(lists(integers(), min_size=1))
    def test_selection_sort(self, elements):
        A = create_array(elements)
        n = len(elements)

        selection_sort(A, n)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))
