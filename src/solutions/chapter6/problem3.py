import math

from book.data_structures import Matrix


def youngify(Y: Matrix, i: int, j: int, m: int, n: int) -> None:
    """Restores the Young tableau property violated by a single element. Moves the violating element downwards or
    rightwards in the matrix.

    Implements:
        Youngify

    Args:
        Y: The Young tableau.
        i: The row index of the element that violates the Young tableau property in Y.
        j: The column index of the element that violates the Young tableau property in Y.
        m: The number of rows of Y.
        n: The number of columns of Y.
    """
    (i_, j_) = (i, j)
    if i < m and Y[i + 1, j] < Y[i_, j_]:
        (i_, j_) = (i + 1, j)
    if j < n and Y[i, j + 1] < Y[i_, j_]:
        (i_, j_) = (i, j + 1)
    if (i_, j_) != (i, j):
        Y[i, j], Y[i_, j_] = Y[i_, j_], Y[i, j]
        youngify(Y, i_, j_, m, n)


def young_extract_min(Y: Matrix, m: int, n: int) -> float:
    """Deletes the smallest element in a Young tableau.

    Implements:
        Young-Extract-Min

    Args:
        Y: The nonempty Young tableau.
        m: The number of rows of Y.
        n: The number of columns of Y.

    Returns:
        The smallest element deleted from Y.
    """
    y = Y[1, 1]
    Y[1, 1] = Y[m, n]
    Y[m, n] = math.inf
    youngify(Y, 1, 1, m, n)
    return y
