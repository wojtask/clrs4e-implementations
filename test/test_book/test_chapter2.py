import unittest

from hamcrest import assert_that, is_, close_to
from hypothesis import given
from hypothesis.strategies import lists, integers, floats
from numpy.polynomial import polynomial

from array_util import create_array, is_sorted, is_permutation
from book.chapter2.problem2 import bubblesort
from book.chapter2.problem3 import horner
from book.chapter2.section1 import insertion_sort, sum_array
from book.chapter2.section3 import merge_sort, insertion_sort_with_binary_search


class TestChapter2(unittest.TestCase):

    @given(lists(integers(), min_size=1))
    def test_insertion_sort(self, elements):
        A = create_array(elements)
        n = len(elements)

        insertion_sort(A, n)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))

    @given(lists(integers(), min_size=1))
    def test_sum_array(self, elements):
        A = create_array(elements)
        n = len(elements)

        actual_sum = sum_array(A, n)

        expected_sum = sum(elements)
        assert_that(actual_sum, is_(expected_sum))

    @given(lists(integers(), min_size=1))
    def test_merge_sort(self, elements):
        A = create_array(elements)
        n = len(elements)

        merge_sort(A, 1, n)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))

    @given(lists(integers(), min_size=1))
    def test_insertion_sort_with_binary_search(self, elements):
        A = create_array(elements)
        n = len(elements)

        insertion_sort_with_binary_search(A, n)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))

    @given(lists(integers(), min_size=1))
    def test_bubblesort(self, elements):
        A = create_array(elements)
        n = len(elements)

        bubblesort(A, n)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))

    @given(lists(floats(min_value=-10.0, max_value=10.0), min_size=1, max_size=5),
           floats(min_value=-10.0, max_value=10.0))
    def test_horner(self, coefficients, x):
        A = create_array(coefficients, start=0)
        n = len(coefficients) - 1

        actual_value = horner(A, n, x)

        expected_value = float(polynomial.polyval(x, coefficients))
        assert_that(actual_value, is_(close_to(expected_value, 1e-7)))
