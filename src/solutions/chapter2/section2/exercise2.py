from book.data_structures import Array
from util import range_of


def selection_sort(A: Array, n: int) -> None:
    """Sorts an array using selection sort.

    Implements:
        Selection-Sort

    Args:
        A: an Array containing the values to be sorted
        n: the number of values to sort
    """
    for i in range_of(1, to=n - 1):
        min = i
        for j in range_of(i + 1, to=n):
            if A[j] < A[min]:
                min = j
        A[min], A[i] = A[i], A[min]
