from book.data_structures import Matrix


def matrix_add_recursive(A: Matrix, B: Matrix, C: Matrix, n: int) -> None:
    """Recursively adds two square matrices and places the result in the third square matrix.

    Implements:
        Matrix-Add-Recursive

    Args:
        A: the first square matrix to add
        B: the second square matrix to add
        C: the matrix to add the matrix sum
        n: the dimension of matrices A and B
    """
    if n == 1:
        C[1, 1] += A[1, 1] + B[1, 1]
        return
    (A11, A12, A21, A22), (B11, B12, B21, B22), (C11, C12, C21, C22) = __partition_matrices(A, B, C, n)
    matrix_add_recursive(A11, B11, C11, n // 2)
    matrix_add_recursive(A12, B12, C12, n // 2)
    matrix_add_recursive(A21, B21, C21, n // 2)
    matrix_add_recursive(A22, B22, C22, n // 2)


def __partition_matrices(A, B, C, n):
    return __partition_matrix(A, n), \
        __partition_matrix(B, n), \
        __partition_matrix(C, n)


def __partition_matrix(M, n):
    return M.submatrix((1, n // 2), (1, n // 2)), \
        M.submatrix((1, n // 2), (n // 2 + 1, n)), \
        M.submatrix((n // 2 + 1, n), (1, n // 2)), \
        M.submatrix((n // 2 + 1, n), (n // 2 + 1, n))
