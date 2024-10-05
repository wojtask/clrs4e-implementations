from book.chapter4.section1 import MatrixPartition
from book.data_structures import Matrix
from util import range_of


def matrix_multiply_recursive_by_copying(A: Matrix, B: Matrix, C: Matrix, n: int) -> None:
    """Recursively multiplies two square matrices and adds the result to the third square matrix. At each recursive step
    partitions the matrices by copying their elements to new submatrices.

    Args:
        A: the first square matrix to multiply
        B: the second square matrix to multiply
        C: the matrix to add the result of the matrix multiplication
        n: the dimension of matrices A and B
    """
    if n == 1:
        C[1, 1] += A[1, 1] * B[1, 1]
        return
    (A11, A12, A21, A22), (B11, B12, B21, B22), (C11, C12, C21, C22) = __partition_matrices_by_copying(A, B, C, n)
    matrix_multiply_recursive_by_copying(A11, B11, C11, n // 2)
    matrix_multiply_recursive_by_copying(A11, B12, C12, n // 2)
    matrix_multiply_recursive_by_copying(A21, B11, C21, n // 2)
    matrix_multiply_recursive_by_copying(A21, B12, C22, n // 2)
    matrix_multiply_recursive_by_copying(A12, B21, C11, n // 2)
    matrix_multiply_recursive_by_copying(A12, B22, C12, n // 2)
    matrix_multiply_recursive_by_copying(A22, B21, C21, n // 2)
    matrix_multiply_recursive_by_copying(A22, B22, C22, n // 2)
    __merge_submatrices_by_copying(C, C11, C12, C21, C22, n)


def __partition_matrices_by_copying(A: Matrix, B: Matrix, C: Matrix, n: int) \
        -> tuple[MatrixPartition, MatrixPartition, MatrixPartition]:
    return __partition_matrix_by_copying(A, n), \
        __partition_matrix_by_copying(B, n), \
        __partition_matrix_by_copying(C, n)


def __partition_matrix_by_copying(M: Matrix, n: int) -> MatrixPartition:
    M11 = Matrix(n // 2, n // 2)
    M12 = Matrix(n // 2, n // 2)
    M21 = Matrix(n // 2, n // 2)
    M22 = Matrix(n // 2, n // 2)
    for i in range_of(1, to=n // 2):
        for j in range_of(1, to=n // 2):
            M11[i, j] = M[i, j]
            M12[i, j] = M[i, n // 2 + j]
            M21[i, j] = M[n // 2 + i, j]
            M22[i, j] = M[n // 2 + i, n // 2 + j]
    return M11, M12, M21, M22


def __merge_submatrices_by_copying(M: Matrix, M11: Matrix, M12: Matrix, M21: Matrix, M22: Matrix, n: int) -> None:
    for i in range_of(1, to=n // 2):
        for j in range_of(1, to=n // 2):
            M[i, j] = M11[i, j]
            M[i, n // 2 + j] = M12[i, j]
            M[n // 2 + i, j] = M21[i, j]
            M[n // 2 + i, n // 2 + j] = M22[i, j]
