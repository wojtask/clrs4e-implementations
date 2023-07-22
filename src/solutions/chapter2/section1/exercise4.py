from book.data_structures import Array
from util import range_of


def linear_search(A: Array, n: int, x: int) -> int | None:
    """Searches for a number in a sequence of numbers.

    Implements pseudocode procedure Linear-Search.

    Args:
        A: an Array containing the sequence of numbers
        n: the number of numbers in the sequence
        x: the number to search for

    Returns:
        An index i such that x equals A[i] or None if x does not appear in A.
    """
    for i in range_of(1, to=n):
        if A[i] == x:
            return i
    return None
