from hypothesis import given
from hypothesis.strategies import lists, integers, floats
from numpy.polynomial import polynomial

from array_util import create_array
from book.chapter2.problem2 import bubblesort
from book.chapter2.problem3 import horner
from book.chapter2.section1 import insertion_sort, sum_array
from book.chapter2.section3 import merge_sort, insertion_sort_with_binary_search
from test_case import ClrsTestCase


class TestChapter2(ClrsTestCase):

    @given(lists(integers(), min_size=1))
    def test_insertion_sort(self, elements):
        A = create_array(elements)
        n = len(elements)

        insertion_sort(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(lists(integers(), min_size=1))
    def test_sum_array(self, elements):
        A = create_array(elements)
        n = len(elements)

        actual_sum = sum_array(A, n)

        expected_sum = sum(elements)
        self.assertEqual(actual_sum, expected_sum)

    @given(lists(integers(), min_size=1))
    def test_merge_sort(self, elements):
        A = create_array(elements)
        n = len(elements)

        merge_sort(A, 1, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(lists(integers(), min_size=1))
    def test_insertion_sort_with_binary_search(self, elements):
        A = create_array(elements)
        n = len(elements)

        insertion_sort_with_binary_search(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(lists(integers(), min_size=1))
    def test_bubblesort(self, elements):
        A = create_array(elements)
        n = len(elements)

        bubblesort(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(lists(floats(min_value=-10.0, max_value=10.0), min_size=1, max_size=5),
           floats(min_value=-10.0, max_value=10.0))
    def test_horner(self, coefficients, x):
        A = create_array(coefficients, start=0)
        n = len(coefficients) - 1

        actual_value = horner(A, n, x)

        expected_value = float(polynomial.polyval(x, coefficients))
        self.assertAlmostEqual(actual_value, expected_value, places=7)
