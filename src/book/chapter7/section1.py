from book.data_structures import Array
from book.data_structures import CT
from util import range_of


def quicksort(A: Array[CT], p: int, r: int) -> None:
    """Sorts an array using quicksort.

    Implements:
        Quicksort

    Args:
        A: an Array containing the values to be sorted
        p: the lower index of the subarray to sort
        r: the upper index of the subarray to sort
    """
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A: Array[CT], p: int, r: int) -> int:
    """Partitions an array into two subarrays, the low side and the high side, such that each element in the low side of
    the partition is less than or equal to the pivot value, which is, in turn, less than or equal to each element in the
    high side.

    Implements:
        Partition

    Args:
        A: an Array to partition
        p: the lower index of the subarray to partition
        r: the upper index of the subarray to partition

    Returns:
        The index q, such that each element in A[p:q - 1] is less than or equal to A[q], and that A[q] is less than or
        equal to each element in A[q + 1:r].
    """
    x = A[r]
    i = p - 1
    for j in range_of(p, to=r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
