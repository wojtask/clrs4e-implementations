from typing import Optional

from book.data_structures import Array


def binary_search(A: Array, x: int, p: int, r: int) -> Optional[int]:
    """Searches for a number in a sorted sequence of numbers.

    Implements pseudocode procedure Binary-Search.

    Args:
        A: an Array containing the sorted sequence of numbers
        x: the number to search for
        p: the lower index of the searched subarray
        r: the upper index of the searched subarray

    Returns:
        An index i such that x equals A[i] or None if x does not appear in A.
    """
    if p > r:
        return None
    q = (p + r) // 2
    if x == A[q]:
        return q
    if x < A[q]:
        return binary_search(A, x, p, q - 1)
    else:
        return binary_search(A, x, q + 1, r)
