from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import floats
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from numpy.polynomial import polynomial

from book.chapter2.problem2 import bubblesort
from book.chapter2.problem3 import horner
from book.chapter2.section1 import insertion_sort
from book.chapter2.section1 import sum_array
from book.chapter2.section3 import insertion_sort_with_binary_search
from book.chapter2.section3 import merge_sort
from test_case import ClrsTestCase
from test_util import create_array


class TestChapter2(ClrsTestCase):

    @given(st.data())
    def test_insertion_sort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        insertion_sort(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_sum_array(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        actual_sum = sum_array(A, n)

        expected_sum = sum(elements)
        self.assertEqual(actual_sum, expected_sum)

    @given(st.data())
    def test_merge_sort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        merge_sort(A, 1, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_insertion_sort_with_binary_search(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        insertion_sort_with_binary_search(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_bubblesort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        bubblesort(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_horner(self, data):
        coefficients = data.draw(lists(floats(min_value=-10.0, max_value=10.0), min_size=1, max_size=5))
        x = data.draw(floats(min_value=-10.0, max_value=10.0))
        A = create_array(coefficients, start=0)
        n = len(coefficients) - 1

        actual_value = horner(A, n, x)

        expected_value = float(polynomial.polyval(x, coefficients))
        self.assertAlmostEqual(actual_value, expected_value, places=7)
