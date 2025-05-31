from book.chapter7.section1 import partition
from book.data_structures import Array
from book.data_structures import CT
from solutions.chapter5.section1.exercise2 import random


def randomized_partition(A: Array[CT], p: int, r: int) -> int:
    """Partitions an array into two subarrays, the low side and the high side, such that each element in the low side of
    the partition is less than or equal to the pivot value, which is, in turn, less than or equal to each element in the
    high side. Chooses the pivot element randomly.

    Implements:
        Randomized-Partition

    Args:
        A: an Array to partition
        p: the lower index of the subarray to partition
        r: the upper index of the subarray to partition

    Returns:
        The index q, such that each element in A[p:q - 1] is less than or equal to A[q], and that A[q] is less than or
        equal to each element in A[q + 1:r].
    """
    i = random(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def randomized_quicksort(A: Array[CT], p: int, r: int) -> None:
    """Sorts an array using the randomized version of quicksort.

    Implements:
        Randomized-Quicksort

    Args:
        A: an Array containing the values to be sorted
        p: the lower index of the subarray to sort
        r: the upper index of the subarray to sort
    """
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)
