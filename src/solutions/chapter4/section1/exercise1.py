from book.chapter4.section1 import matrix_multiply_recursive
from book.data_structures import Matrix
from util import range_of


def matrix_multiply_recursive_general(A: Matrix, B: Matrix, C: Matrix, n: int) -> None:
    """A generalized version of the recursive algorithm for multiplying two square matrices, supporting arbitrary matrix
     dimensions.

    Args:
        A: the first square matrix to multiply
        B: the second square matrix to multiply
        C: the matrix to add to the result of the matrix multiplication
        n: the dimension of matrices A and B
    """
    m = __next_power_of_2(n)
    A_ = __extend_matrix(A, n, m)
    B_ = __extend_matrix(B, n, m)
    C_ = __extend_matrix(C, n, m)
    matrix_multiply_recursive(A_, B_, C_, m)
    __copy_result(C_, C, n)


def __next_power_of_2(n: int) -> int:
    res = 1
    while res < n:
        res *= 2
    return res


def __extend_matrix(source: Matrix, source_size: int, extended_size: int) -> Matrix:
    extended = Matrix(extended_size, extended_size)
    for i in range_of(1, to=source_size):
        for j in range_of(1, to=source_size):
            extended[i, j] = source[i, j]
    return extended


def __copy_result(extended: Matrix, original: Matrix, original_size: int) -> None:
    for i in range_of(1, to=original_size):
        for j in range_of(1, to=original_size):
            original[i, j] = extended[i, j]
