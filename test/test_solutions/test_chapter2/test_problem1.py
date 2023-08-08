from unittest import TestCase

from hamcrest import assert_that
from hypothesis import given
from hypothesis.strategies import lists, integers

from array_util import create_array, is_sorted, is_permutation
from solutions.chapter2.problem1 import merge_sort_with_insertion_sort


class TestMergeSortWithInsertionSort(TestCase):

    @given(lists(integers(), min_size=1), integers(min_value=1))
    def test_merge_sort_with_insertion_sort(self, elements, k):
        A = create_array(elements)
        n = len(elements)

        merge_sort_with_insertion_sort(A, 1, n, k)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))
