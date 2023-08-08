import operator

from hypothesis import given
from hypothesis.strategies import lists, integers, composite, floats
from numpy.polynomial import polynomial

from array_util import create_array
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
from util import range_of


def binary_to_decimal(A, n):
    result = 0
    for i in range_of(0, to=n - 1):
        result += A[i] * 2 ** i
    return result


@composite
def operands_in_binary(draw):
    n = draw(integers(min_value=1, max_value=63))
    operand1 = draw(lists(integers(min_value=0, max_value=1), min_size=n, max_size=n))
    operand2 = draw(lists(integers(min_value=0, max_value=1), min_size=n, max_size=n))
    return operand1, operand2


def count_inversions_naive(elements):
    A = create_array(elements)
    n = len(elements)
    inversions = 0
    for i in range_of(1, to=n - 1):
        for j in range_of(i + 1, to=n):
            if A[i] > A[j]:
                inversions += 1
    return inversions


class TestChapter2(ClrsTestCase):

    @given(lists(integers(), min_size=1))
    def test_insertion_sort_decreasing(self, elements):
        A = create_array(elements)
        n = len(elements)

        insertion_sort_decreasing(A, n)

        self.assertArraySorted(A, end=n, cmp=operator.ge)
        self.assertArrayPermuted(A, elements, end=n)

    @given(lists(integers(min_value=-10, max_value=10), min_size=1, max_size=20),
           integers(min_value=-10, max_value=10))
    def test_linear_search(self, elements, x):
        A = create_array(elements)
        n = len(elements)

        actual_index = linear_search(A, n, x)

        if actual_index:
            self.assertEqual(A[actual_index], x)
        else:
            self.assertNotIn(x, elements)

    @given(operands_in_binary())
    def test_add_binary_integers(self, operands):
        A = create_array(operands[0], start=0)
        B = create_array(operands[1], start=0)
        n = len(operands[0])
        a = binary_to_decimal(A, n)
        b = binary_to_decimal(B, n)

        C = add_binary_integers(A, B, n)

        c = binary_to_decimal(C, n + 1)
        self.assertEqual(c, a + b)

    @given(lists(integers(), min_size=1))
    def test_selection_sort(self, elements):
        A = create_array(elements)
        n = len(elements)

        selection_sort(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(lists(integers(), min_size=1))
    def test_recursive_insertion_sort(self, elements):
        A = create_array(elements)
        n = len(elements)

        recursive_insertion_sort(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(lists(integers(min_value=-10, max_value=10), min_size=1, max_size=20).map(sorted),
           integers(min_value=-10, max_value=10))
    def test_binary_search(self, elements, x):
        A = create_array(elements)
        n = len(elements)

        actual_index = binary_search(A, 1, n, x)

        if actual_index:
            self.assertEqual(A[actual_index], x)
        else:
            self.assertNotIn(x, elements)

    @given(lists(integers(min_value=-10, max_value=10), min_size=1, unique=True),
           integers(min_value=-20, max_value=20))
    def test_sum_search_positive(self, elements, x):
        A = create_array(elements)
        n = len(elements)

        actual_found = sum_search(A, n, x)

        all_sums = {a + b for a in elements for b in elements if a != b}
        expected_found = x in all_sums
        self.assertEqual(actual_found, expected_found)

    @given(lists(integers(), min_size=1), integers(min_value=1))
    def test_merge_sort_with_insertion_sort(self, elements, k):
        A = create_array(elements)
        n = len(elements)

        merge_sort_with_insertion_sort(A, 1, n, k)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(lists(floats(min_value=-10.0, max_value=10.0), min_size=1, max_size=5),
           floats(min_value=-10.0, max_value=10.0))
    def test_polynomial_evaluate(self, coefficients, x):
        A = create_array(coefficients, start=0)
        n = len(coefficients) - 1

        actual_value = polynomial_evaluate(A, n, x)

        expected_value = float(polynomial.polyval(x, coefficients))
        self.assertAlmostEqual(actual_value, expected_value, places=7)

    @given(lists(integers(), min_size=1))
    def test_count_inversions(self, elements):
        A = create_array(elements)
        n = len(elements)

        actual_inversions = count_inversions(A, 1, n)

        expected_inversions = count_inversions_naive(elements)
        self.assertEqual(actual_inversions, expected_inversions)
