from book.chapter2.section3 import merge_sort
from book.data_structures import Array
from solutions.chapter2.section3.exercise6 import binary_search


def sum_search(A: Array[int], n: int, x: int) -> bool:
    """Determines whether a set of integers contains two elements that sum to a given value.

    Args:
        A: an Array representing the set of integers
        n: the number of numbers in the set
        x: the sum to search for

    Returns:
        True iff the set represented by the array A contains two elements that sum to exactly x.
    """
    merge_sort(A, 1, n)
    i = 1
    while i < n and A[i] < x / 2:
        if binary_search(A, i + 1, n, x - A[i]) is not None:
            return True
        i += 1
    return False
