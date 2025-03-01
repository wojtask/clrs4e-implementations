from __future__ import annotations

from book.data_structures import Array
from book.data_structures import CT
from util import range_of


def linear_search(A: Array[CT], n: int, x: CT) -> int | None:
    """Searches for a value in a sequence using linear search.

    Implements:
        Linear-Search

    Args:
        A: an Array containing the sequence of values
        n: the number of values in the sequence
        x: the value to search for

    Returns:
        An index i such that x equals A[i] or None if x does not appear in A.
    """
    for i in range_of(1, to=n):
        if A[i] == x:
            return i
    return None
