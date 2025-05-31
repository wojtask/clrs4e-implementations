from book.data_structures import Array
from book.data_structures import CT


def stooge_sort(A: Array[CT], p: int, r: int) -> None:
    """Sorts an array using stooge sort.

    Implements:
        Stooge-Sort

    Args:
        A: an Array containing the values to be sorted
        p: the lower index of the subarray to sort
        r: the upper index of the subarray to sort
    """
    if A[p] > A[r]:
        A[p], A[r] = A[r], A[p]
    if p + 1 < r:
        k = (r - p + 1) // 3
        stooge_sort(A, p, r - k)
        stooge_sort(A, p + k, r)
        stooge_sort(A, p, r - k)
