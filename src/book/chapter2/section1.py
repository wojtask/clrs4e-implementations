from book.data_structures import Array
from util import range_of


def insertion_sort(A: Array, n: int) -> None:
    """Reorders a sequence of values according to their "<=" relation.

    Implements pseudocode procedure Insertion-Sort from Section 2.1 of the book.

    Args:
        A: an Array containing the values to be sorted
        n: the number of values to sort
    """
    for i in range_of(2, to=n):
        key = A[i]
        j = i - 1
        while j > 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
