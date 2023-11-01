import numpy
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from book.data_structures import Matrix
from solutions.chapter4.section1.exercise1 import matrix_multiply_recursive_general
from test_case import ClrsTestCase
from test_util import create_matrix


class TestChapter4(ClrsTestCase):

    @given(st.data())
    def test_matrix_multiply_recursive_general(self, data):
        n = data.draw(integers(min_value=1, max_value=15), label="Matrices dimension")
        elements1 = data.draw(
            lists(lists(integers(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="First matrix elements")
        elements2 = data.draw(
            lists(lists(integers(min_value=-1000, max_value=1000), min_size=n, max_size=n), min_size=n, max_size=n),
            label="Second matrix elements")
        A = create_matrix(elements1)
        B = create_matrix(elements2)
        C = Matrix(n, n)

        matrix_multiply_recursive_general(A, B, C, n)

        actual_product = create_matrix(numpy.matmul(elements1, elements2))

        self.assertEqual(C, actual_product)
