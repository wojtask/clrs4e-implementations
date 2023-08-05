from typing import Optional

from book.data_structures import Array


def binary_search(A: Array, p: int, r: int, x: int) -> Optional[int]:
    """Searches for a number in a sorted sequence of numbers using binary serach.

    Implements:
        Binary-Search

    Args:
        A: an Array containing the sorted sequence of numbers
        p: the lower index of the searched subarray
        r: the upper index of the searched subarray
        x: the number to search for

    Returns:
        An index i such that x equals A[i] or None if x does not appear in A.
    """
    if p > r:
        return None
    q = (p + r) // 2
    if x == A[q]:
        return q
    if x < A[q]:
        return binary_search(A, p, q - 1, x)
    else:
        return binary_search(A, q + 1, r, x)
