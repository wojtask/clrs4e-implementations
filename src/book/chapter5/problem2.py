from typing import Optional

from book.chapter5.section3 import randomly_permute
from book.data_structures import Array
from util import range_of


def deterministic_search(A: Array, n: int, x: int) -> Optional[int]:
    """Searches for a value in an array, examining its elements sequentially.

    Implements:
        Deterministic-Search

    Args:
        A: an Array to search through
        n: the number of numbers in array A
        x: the value to search for

    Returns:
        An index i such that x equals A[i] or None if x does not appear in A.
    """
    for i in range_of(1, to=n):
        if A[i] == x:
            return i
    return None


def scramble_search(A: Array, n: int, x: int) -> Optional[int]:
    """Searches for a value in an array by first permuting it, then examining its elements sequentially.

    Implements:
        Scramble-Search

    Args:
        A: an Array to search through
        n: the number of numbers in array A
        x: the value to search for

    Returns:
        An index i such that x equals A[i] or None if x does not appear in A.
    """
    randomly_permute(A, n)
    return deterministic_search(A, n, x)
