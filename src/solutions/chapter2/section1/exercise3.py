from book.data_structures import Array
from util import range_of


def insertion_sort_decreasing(A: Array, n: int) -> None:
    """Sorts an array into monotonically decreasing order using insertion sort.

    Args:
        A: an Array containing the values to be sorted
        n: the number of values to sort
    """
    for i in range_of(2, to=n):
        key = A[i]
        j = i - 1
        while j > 0 and A[j] < key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
