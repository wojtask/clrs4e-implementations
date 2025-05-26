import numpy
from hypothesis import assume
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import complex_numbers
from hypothesis.strategies import floats
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from hypothesis.strategies import sampled_from

from book.chapter4.section1 import matrix_multiply
from book.data_structures import Matrix
from solutions.chapter4.problem6 import BadChipStrategy
from solutions.chapter4.problem6 import Chip
from solutions.chapter4.problem6 import ChipCondition
from solutions.chapter4.problem6 import identify_all_good_chips
from solutions.chapter4.problem7 import monge_leftmost_minimums
from solutions.chapter4.section1.exercise1 import matrix_multiply_recursive_general
from solutions.chapter4.section1.exercise3 import matrix_multiply_recursive_by_copying
from solutions.chapter4.section1.exercise4 import matrix_add_recursive
from solutions.chapter4.section2.exercise2 import strassen
from solutions.chapter4.section2.exercise5 import complex_multiply
from solutions.chapter4.section2.exercise6 import matrix_multiply_by_squaring
from test_case import ClrsTestCase
from test_util import create_array
from test_util import create_matrix
from util import range_of


def is_monge_array(A: Matrix, m: int, n: int) -> bool:
    for i in range_of(1, to=m - 1):
        for j in range_of(1, to=n - 1):
            if A[i, j] + A[i + 1, j + 1] > A[i, j + 1] + A[i + 1, j]:
                return False
    return True


class TestChapter4(ClrsTestCase):

    @given(st.data())
    def test_matrix_multiply_recursive_general(self, data):
        n = data.draw(integers(min_value=1, max_value=15), label="Matrices dimension")
        elements1 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="First matrix elements")
        elements2 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="Second matrix elements")
        A = create_matrix(elements1)
        B = create_matrix(elements2)
        C = Matrix(n, n)

        matrix_multiply_recursive_general(A, B, C, n)

        expected_product = create_matrix(numpy.matmul(elements1, elements2))
        self.assertEqual(C, expected_product)

    @given(st.data())
    def test_matrix_multiply_recursive_by_copying(self, data):
        k = data.draw(integers(min_value=0, max_value=4), label="Matrices dimension exponent")
        n = 2 ** k
        elements1 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="First matrix elements")
        elements2 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="Second matrix elements")
        A = create_matrix(elements1)
        B = create_matrix(elements2)
        C = Matrix(n, n)

        matrix_multiply_recursive_by_copying(A, B, C, n)

        expected_product = create_matrix(numpy.matmul(elements1, elements2))
        self.assertEqual(C, expected_product)

    @given(st.data())
    def test_matrix_add_recursive(self, data):
        k = data.draw(integers(min_value=0, max_value=4), label="Matrices dimension exponent")
        n = 2 ** k
        elements1 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="First matrix elements")
        elements2 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="Second matrix elements")
        A = create_matrix(elements1)
        B = create_matrix(elements2)
        C = Matrix(n, n)

        matrix_add_recursive(A, B, C, n)

        expected_sum = create_matrix(numpy.add(elements1, elements2))
        self.assertEqual(C, expected_sum)

    @given(st.data())
    def test_strassen(self, data):
        k = data.draw(integers(min_value=0, max_value=4), label="Matrices dimension exponent")
        n = 2 ** k
        elements1 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="First matrix elements")
        elements2 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="Second matrix elements")
        A = create_matrix(elements1)
        B = create_matrix(elements2)
        C = Matrix(n, n)

        strassen(A, B, C, n)

        expected_product = create_matrix(numpy.matmul(elements1, elements2))
        self.assertEqual(C, expected_product)

    @given(st.data())
    def test_complex_multiply(self, data):
        z1 = data.draw(complex_numbers(max_magnitude=1000.0), label="First complex number")
        z2 = data.draw(complex_numbers(max_magnitude=1000.0), label="Second complex number")

        real, imag = complex_multiply(z1.real, z1.imag, z2.real, z2.imag)

        actual_product = complex(real, imag)
        expected_product = z1 * z2
        self.assertAlmostEqual(actual_product, expected_product, places=7)

    @given(st.data())
    def test_matrix_multiply_by_squaring(self, data):
        n = data.draw(integers(min_value=1, max_value=15), label="Matrices dimension")
        elements1 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="First matrix elements")
        elements2 = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="Second matrix elements")
        A = create_matrix(elements1)
        B = create_matrix(elements2)
        C = Matrix(n, n)

        def matrix_square_function(D: Matrix, E: Matrix, m: int) -> None:
            matrix_multiply(D, D, E, m)

        matrix_multiply_by_squaring(A, B, C, matrix_square_function, n)

        expected_product = create_matrix(numpy.matmul(elements1, elements2))
        self.assertEqual(C, expected_product)

    @given(st.data())
    def test_identify_all_good_chips(self, data):
        n = data.draw(integers(min_value=1, max_value=1000), label="The number of all chips")
        good_chips_number = data.draw(integers(min_value=n // 2 + 1, max_value=n), label="The number of good chips")
        bad_chip_strategy = data.draw(sampled_from(BadChipStrategy))
        chips = (set(Chip(ChipCondition.GOOD) for _ in range_of(1, to=good_chips_number))
                 | set(Chip(ChipCondition.BAD) for _ in range_of(good_chips_number + 1, to=n)))

        actual_good_chips = identify_all_good_chips(chips, strategy=bad_chip_strategy)

        self.assertEqual(len(actual_good_chips), good_chips_number)
        for chip in actual_good_chips:
            self.assertEqual(chip.condition, ChipCondition.GOOD)

    @given(st.data())
    def test_monge_leftmost_minimums(self, data):
        m = data.draw(integers(min_value=1, max_value=15), label="Monge array row dimension")
        n = data.draw(integers(min_value=1, max_value=15), label="Monge array column dimension")
        elements = data.draw(
            lists(lists(floats(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=m, max_size=m),
            label="Monge array elements")
        A = create_matrix(elements)
        assume(is_monge_array(A, m, n))

        actual_minimums = monge_leftmost_minimums(A, m, n)

        expected_minimums = create_array([min(row) for row in elements])
        self.assertEqual(actual_minimums, expected_minimums)
