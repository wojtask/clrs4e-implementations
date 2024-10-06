import operator

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import floats
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from numpy.polynomial import polynomial

from book.data_structures import CT
from solutions.chapter2.problem1 import merge_sort_with_insertion_sort
from solutions.chapter2.problem3 import polynomial_evaluate
from solutions.chapter2.problem4 import count_inversions
from solutions.chapter2.section1.exercise3 import insertion_sort_decreasing
from solutions.chapter2.section1.exercise4 import linear_search
from solutions.chapter2.section1.exercise5 import add_binary_integers
from solutions.chapter2.section2.exercise2 import selection_sort
from solutions.chapter2.section3.exercise5 import recursive_insertion_sort
from solutions.chapter2.section3.exercise6 import binary_search
from solutions.chapter2.section3.exercise8 import sum_search
from test_case import ClrsTestCase
from test_util import binary_to_decimal
from test_util import create_array
from util import range_of


def count_inversions_naive(elements: list[CT]) -> int:
    A = create_array(elements)
    n = len(elements)
    inversions = 0
    for i in range_of(1, to=n - 1):
        for j in range_of(i + 1, to=n):
            if A[i] > A[j]:
                inversions += 1
    return inversions


class TestChapter2(ClrsTestCase):

    @given(st.data())
    def test_insertion_sort_decreasing(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        insertion_sort_decreasing(A, n)

        self.assertArraySorted(A, end=n, cmp=operator.ge)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_linear_search(self, data):
        elements = data.draw(lists(integers(min_value=-10, max_value=10), min_size=1, max_size=20))
        x = data.draw(integers(min_value=-10, max_value=10))
        A = create_array(elements)
        n = len(elements)

        actual_index = linear_search(A, n, x)

        if actual_index:
            self.assertEqual(A[actual_index], x)
        else:
            self.assertNotIn(x, elements)

    @given(st.data())
    def test_add_binary_integers(self, data):
        n = data.draw(integers(min_value=1, max_value=10))
        operand1 = data.draw(lists(integers(min_value=0, max_value=1), min_size=n, max_size=n))
        operand2 = data.draw(lists(integers(min_value=0, max_value=1), min_size=n, max_size=n))
        A = create_array(operand1, start=0)
        B = create_array(operand2, start=0)
        a = binary_to_decimal(A, n)
        b = binary_to_decimal(B, n)

        C = add_binary_integers(A, B, n)

        c = binary_to_decimal(C, n + 1)
        self.assertEqual(c, a + b)

    @given(st.data())
    def test_selection_sort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        selection_sort(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_recursive_insertion_sort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        recursive_insertion_sort(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_binary_search(self, data):
        elements = data.draw(lists(integers(min_value=-10, max_value=10), min_size=1, max_size=20).map(sorted))
        x = data.draw(integers(min_value=-10, max_value=10))
        A = create_array(elements)
        n = len(elements)

        actual_index = binary_search(A, 1, n, x)

        if actual_index:
            self.assertEqual(A[actual_index], x)
        else:
            self.assertNotIn(x, elements)

    @given(st.data())
    def test_sum_search_positive(self, data):
        elements = data.draw(lists(integers(min_value=-10, max_value=10), min_size=1, unique=True))
        x = data.draw(integers(min_value=-20, max_value=20))
        A = create_array(elements)
        n = len(elements)

        actual_found = sum_search(A, n, x)

        all_sums = {a + b for a in elements for b in elements if a != b}
        expected_found = x in all_sums
        self.assertEqual(actual_found, expected_found)

    @given(st.data())
    def test_merge_sort_with_insertion_sort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        k = data.draw(integers(min_value=1))
        A = create_array(elements)
        n = len(elements)

        merge_sort_with_insertion_sort(A, 1, n, k)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_polynomial_evaluate(self, data):
        coefficients = data.draw(lists(floats(min_value=-10.0, max_value=10.0), min_size=1, max_size=5))
        x = data.draw(floats(min_value=-10.0, max_value=10.0))
        A = create_array(coefficients, start=0)
        n = len(coefficients) - 1

        actual_value = polynomial_evaluate(A, n, x)

        expected_value = float(polynomial.polyval(x, coefficients))
        self.assertAlmostEqual(actual_value, expected_value, places=7)

    @given(st.data())
    def test_count_inversions(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        actual_inversions = count_inversions(A, 1, n)

        expected_inversions = count_inversions_naive(elements)
        self.assertEqual(actual_inversions, expected_inversions)
