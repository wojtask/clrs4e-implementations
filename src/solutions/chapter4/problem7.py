from __future__ import annotations

from book.data_structures import Array
from book.data_structures import Matrix
from util import ceil_div
from util import range_of


def monge_leftmost_minimums(A: Matrix, m: int, n: int) -> Array[int]:
    """Finds the leftmost minimum in each row of a Monge array.

    Args:
        A: a Monge array
        m: the number of rows of A
        n: the number of columns of A

    Returns:
        The array containing the leftmost minimums of A, ordered by rows.
    """
    indices = __monge_leftmost_minimums_indices(A, m, n)
    minimums = Array[int](1, m)
    for i in range_of(1, to=m):
        minimums[i] = A[i, indices[i]]
    return minimums


def __monge_leftmost_minimums_indices(A: Matrix, m: int, n: int) -> Array[int]:
    indices = Array[int](1, m)
    if m == 1:
        indices[1] = __find_minimum_index(A, 1, 1, n)
        return indices
    A_ = A.even_rows_submatrix()
    even_rows_leftmost_minimums_indices = __monge_leftmost_minimums_indices(A_, m // 2, n)
    odd_rows_leftmost_minimums_indices = __monge_odd_rows_leftmost_minimums_indices(A, m, n,
                                                                                    even_rows_leftmost_minimums_indices)
    for i in range_of(1, to=m // 2):
        indices[2 * i] = even_rows_leftmost_minimums_indices[i]
    for i in range_of(1, to=ceil_div(m, 2)):
        indices[2 * i - 1] = odd_rows_leftmost_minimums_indices[i]
    return indices


def __monge_odd_rows_leftmost_minimums_indices(A: Matrix,
                                               m: int,
                                               n: int,
                                               even_rows_leftmost_minimums_indices: Array[int]) -> Array[int]:
    odd_rows_leftmost_minimums_indices = Array[int](1, ceil_div(m, 2))
    for i in range_of(1, to=ceil_div(m, 2)):
        prev_minimum_index = even_rows_leftmost_minimums_indices[i - 1] if i > 1 else 1
        next_minimum_index = even_rows_leftmost_minimums_indices[i] if i <= m // 2 else n
        odd_rows_leftmost_minimums_indices[i] = __find_minimum_index(A, 2 * i - 1, prev_minimum_index,
                                                                     next_minimum_index)
    return odd_rows_leftmost_minimums_indices


def __find_minimum_index(A: Matrix, row: int, col_start: int, col_end: int) -> int:
    minimum = A[row, col_start]
    index = col_start
    for j in range_of(col_start + 1, to=col_end):
        if A[row, j] < minimum:
            minimum = A[row, j]
            index = j
    return index
