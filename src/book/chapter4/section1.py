from book.data_structures import Matrix
from util import range_of


def matrix_multiply(A: Matrix, B: Matrix, C: Matrix, n: int) -> None:
    """Multiplies two square matrices and adds the result to the third square matrix.

    Implements:
        Matrix-Multiply

    Args:
        A: the first square matrix to multiply
        B: the second square matrix to multiply
        C: the matrix to add the result of the matrix multiplication
        n: the dimension of matrices A and B
    """
    for i in range_of(1, to=n):
        for j in range_of(1, to=n):
            for k in range_of(1, to=n):
                C[i, j] += A[i, k] * B[k, j]
