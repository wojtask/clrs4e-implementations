from typing import Optional
from typing import Union

from book.data_structures import Array
from book.data_structures import Matrix
from util import ceil_div
from util import range_of


def monge_leftmost_minimums(A: Matrix, m: int, n: int) -> Array[Union[int, float]]:
    """Finds the leftmost minimum in each row of a Monge array.

    Args:
        A: a Monge array
        m: the number of rows of A
        n: the number of columns of A

    Returns:
        The array containing the leftmost minimums of A, ordered by rows.
    """
    indices = __monge_leftmost_minimums_indices(A, m, n)
    minimums = Array(1, m)
    for i in range_of(1, to=m):
        minimums[i] = A[i, indices[i]]
    return minimums


def __monge_leftmost_minimums_indices(A: Matrix, m: int, n: int) -> Optional[Array[Union[int, float]]]:
    if m == 0:
        return None
    A_ = A.even_rows_submatrix()
    even_rows_leftmost_minimums_indices = __monge_leftmost_minimums_indices(A_, m // 2, n)
    odd_rows_leftmost_minimums_indices = __monge_odd_rows_leftmost_minimums_indices(A, m, n,
                                                                                    even_rows_leftmost_minimums_indices)
    indices = Array(1, m)
    for i in range_of(1, to=m // 2):
        indices[2 * i] = even_rows_leftmost_minimums_indices[i]
    for i in range_of(1, to=ceil_div(m, 2)):
        indices[2 * i - 1] = odd_rows_leftmost_minimums_indices[i]
    return indices


def __monge_odd_rows_leftmost_minimums_indices(A: Matrix, m: int, n: int,
                                               even_rows_leftmost_minimums_indices: Array[Union[int, float]]) \
        -> Array[Union[int, float]]:
    odd_rows_leftmost_minimums_indices = Array(1, ceil_div(m, 2))
    for i in range_of(1, to=ceil_div(m, 2)):
        prev_minimum_index = even_rows_leftmost_minimums_indices[i - 1] if i > 1 else 1
        next_minimum_index = even_rows_leftmost_minimums_indices[i] if i <= m // 2 else n
        row_number = 2 * i - 1
        minimum = None
        for j in range_of(prev_minimum_index, to=next_minimum_index):
            if minimum is None or A[row_number, j] < minimum:
                minimum = A[row_number, j]
                odd_rows_leftmost_minimums_indices[i] = j
    return odd_rows_leftmost_minimums_indices
