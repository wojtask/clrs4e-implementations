from unittest import TestCase

from hamcrest import assert_that
from hypothesis import given
from hypothesis.strategies import lists, integers

from array_util import create_array, is_sorted, is_permutation
from book.chapter2.section3 import merge_sort, insertion_sort_with_binary_search


class TestMergeSort(TestCase):

    @given(lists(integers(), min_size=1))
    def test_merge_sort(self, elements):
        A = create_array(elements)
        n = len(elements)

        merge_sort(A, 1, n)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))


class TestInsertionSortWithBinarySearch(TestCase):

    @given(lists(integers(), min_size=1))
    def test_insertion_sort_with_binary_search(self, elements):
        A = create_array(elements)
        n = len(elements)

        insertion_sort_with_binary_search(A, n)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))
