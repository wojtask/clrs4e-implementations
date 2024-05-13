from typing import Callable

from book.data_structures import Matrix
from solutions.chapter4.section2.exercise2 import matrix_add
from util import range_of


def matrix_multiply_by_squaring(
        A: Matrix,
        B: Matrix,
        C: Matrix,
        matrix_square: Callable[[Matrix, Matrix, int], None],
        n: int,
) -> None:
    """Multiplies two square matrices and adds the result to the third square matrix, using a function for squaring
    matrices.

    Args:
        A: the first square matrix to multiply
        B: the second square matrix to multiply
        C: the matrix to add the result of the matrix multiplication
        matrix_square: a function for squaring matrices.
            The first argument is the square matrix to square, the second argument is the matrix to accumulate the
            result, and the third argument is the dimension of the input matrix.
        n: the dimension of matrices A and B
    """
    D = __create_padded_input_matrix(A, B, n)
    E = Matrix(2 * n, 2 * n)
    matrix_square(D, E, 2 * n)
    matrix_add(C, E.submatrix((1, n), (n + 1, 2 * n)), C, n)


def __create_padded_input_matrix(A: Matrix, B: Matrix, n: int) -> Matrix:
    M = Matrix(2 * n, 2 * n)
    for i in range_of(1, to=n):
        for j in range_of(1, to=n):
            M[i, j] = A[i, j]
            M[i, n + j] = B[i, j]
    return M
