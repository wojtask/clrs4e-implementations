from typing import Iterable
from typing import Tuple

from book.chapter4.section1 import MatrixPartition
from book.data_structures import Matrix
from util import range_of


def strassen(A: Matrix, B: Matrix, C: Matrix, n: int) -> None:
    """Multiplies two square matrices and adds the result to the third square matrix, using Strassen's algorithm.

    Args:
        A: the first square matrix to multiply
        B: the second square matrix to multiply
        C: the matrix to add the result of the matrix multiplication
        n: the dimension of matrices A and B
    """
    if n == 1:
        C[1, 1] += A[1, 1] * B[1, 1]
        return
    (A11, A12, A21, A22), (B11, B12, B21, B22), (C11, C12, C21, C22) = __partition_matrices(A, B, C, n)
    (S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, P1, P2, P3, P4, P5, P6, P7) = __create_intermediate_matrices(n // 2)
    matrix_subtract(B12, B22, S1, n // 2)
    matrix_add(A11, A12, S2, n // 2)
    matrix_add(A21, A22, S3, n // 2)
    matrix_subtract(B21, B11, S4, n // 2)
    matrix_add(A11, A22, S5, n // 2)
    matrix_add(B11, B22, S6, n // 2)
    matrix_subtract(A12, A22, S7, n // 2)
    matrix_add(B21, B22, S8, n // 2)
    matrix_subtract(A11, A21, S9, n // 2)
    matrix_add(B11, B12, S10, n // 2)
    strassen(A11, S1, P1, n // 2)
    strassen(S2, B22, P2, n // 2)
    strassen(S3, B11, P3, n // 2)
    strassen(A22, S4, P4, n // 2)
    strassen(S5, S6, P5, n // 2)
    strassen(S7, S8, P6, n // 2)
    strassen(S9, S10, P7, n // 2)
    matrix_add(P5, P4, C11, n // 2)
    matrix_subtract(P6, P2, C11, n // 2)
    matrix_add(P1, P2, C12, n // 2)
    matrix_add(P3, P4, C21, n // 2)
    matrix_subtract(P5, P3, C22, n // 2)
    matrix_subtract(P1, P7, C22, n // 2)


def __partition_matrices(A: Matrix, B: Matrix, C: Matrix, n: int) \
        -> Tuple[MatrixPartition, MatrixPartition, MatrixPartition]:
    return __partition_matrix(A, n), \
        __partition_matrix(B, n), \
        __partition_matrix(C, n)


def __partition_matrix(M: Matrix, n: int) -> MatrixPartition:
    return M.submatrix((1, n // 2), (1, n // 2)), \
        M.submatrix((1, n // 2), (n // 2 + 1, n)), \
        M.submatrix((n // 2 + 1, n), (1, n // 2)), \
        M.submatrix((n // 2 + 1, n), (n // 2 + 1, n))


def __create_intermediate_matrices(n: int) -> Iterable[Matrix]:
    return [Matrix(n, n) for _ in range_of(1, to=17)]


def matrix_add(A: Matrix, B: Matrix, C: Matrix, n: int) -> None:
    for i in range_of(1, to=n):
        for j in range_of(1, to=n):
            C[i, j] += A[i, j] + B[i, j]


def matrix_subtract(A: Matrix, B: Matrix, C: Matrix, n: int) -> None:
    for i in range_of(1, to=n):
        for j in range_of(1, to=n):
            C[i, j] += A[i, j] - B[i, j]
