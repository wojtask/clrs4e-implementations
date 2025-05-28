import math

from book.data_structures import Array
from book.data_structures import Matrix
from util import range_of


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


def reversed_youngify(Y: Matrix, i: int, j: int) -> None:
    """Restores the Young tableau property violated by a single element. Moves the violating element upwards or
    leftwards in the matrix.

    Implements:
        Reversed-Youngify

    Args:
        Y: The Young tableau.
        i: The row index of the element that violates the Young tableau property in Y.
        j: The column index of the element that violates the Young tableau property in Y.
    """
    (i_, j_) = (i, j)
    if i > 1 and Y[i - 1, j] > Y[i_, j_]:
        (i_, j_) = (i - 1, j)
    if j > 1 and Y[i, j - 1] > Y[i_, j_]:
        (i_, j_) = (i, j - 1)
    if (i_, j_) != (i, j):
        Y[i, j], Y[i_, j_] = Y[i_, j_], Y[i, j]
        reversed_youngify(Y, i_, j_)


def young_insert(Y: Matrix, m: int, n: int, k: float) -> None:
    """Inserts a new element into a Young tableau.

    Implements:
        Young-Insert

    Args:
        Y: The nonfull Young tableau.
        m: The number of rows of Y.
        n: The number of columns of Y.
        k: The element to insert into Y.
    """
    Y[m, n] = k
    reversed_youngify(Y, m, n)


def young_sort(A: Array[float], n: int) -> None:
    """Sorts an array using a Young tableau.

    Implements:
        Young-Sort

    Args:
        A: The aray of n^2 numbers to sort.
        n: The square root of the number of values to sort.
    """
    Y = Matrix(n, n)
    for i in range_of(1, to=n):
        for j in range_of(1, to=n):
            Y[i, j] = math.inf
    for i in range_of(1, to=n ** 2):
        young_insert(Y, n, n, A[i])
    for i in range_of(1, to=n ** 2):
        A[i] = young_extract_min(Y, n, n)


def young_search(Y, m: int, n: int, k: float) -> bool:
    """Determines whether a Young tableau contains a value.

    Implement:
        Young-Search

    Args:
        Y: The Young tableau.
        m: The number of rows of Y.
        n: The number of columns of Y.
        k: The value to search for.

    Returns:
        True iff Y contains k.
    """
    i = 1
    j = n
    while i <= m and j >= 1:
        if k == Y[i, j]:
            return True
        if k > Y[i, j]:
            i += 1
        else:
            j -= 1
    return False
