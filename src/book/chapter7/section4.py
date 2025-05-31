from book.chapter7.section1 import partition
from book.data_structures import Array
from book.data_structures import CT
from solutions.chapter5.section1.exercise2 import random
from util import range_of


def insertion_quicksort(A: Array[CT], p: int, r: int, k: int) -> None:
    """Sorts an array using quicksort, if the array size exceeds a given threshold, and using insertion sort otherwise.

    Args:
        A: an Array containing the values to be sorted
        p: the lower index of the subarray to sort
        r: the upper index of the subarray to sort
        k: the threshold of the subarray size below which the subarray is to be sorted using insertion sort
    """
    if p < r:
        if r - p + 1 >= k:
            q = partition(A, p, r)
            insertion_quicksort(A, p, q - 1, k)
            insertion_quicksort(A, q + 1, r, k)
        else:
            for i in range_of(p + 1, to=r):
                key = A[i]
                j = i - 1
                while j > 0 and A[j] > key:
                    A[j + 1] = A[j]
                    j -= 1
                A[j + 1] = key


def median_of_3_partition(A: Array[CT], p: int, r: int) -> int:
    """Partitions an array into two subarrays, the low side and the high side, such that each element in the low side of
    the partition is less than or equal to the pivot value, which is, in turn, less than or equal to each element in the
    high side. Uses a median of randomly picked three elements as the pivot.

    Args:
        A: an Array to partition
        p: the lower index of the subarray to partition
        r: the upper index of the subarray to partition

    Returns:
        The index q, such that each element in A[p:q - 1] is less than or equal to A[q], and that A[q] is less than or
        equal to each element in A[q + 1:r].
    """
    i1, i2, i3 = random(p, r), random(p, r), random(p, r)
    if A[i2] <= A[i1] <= A[i3] or A[i3] <= A[i1] <= A[i2]:
        m = i1
    elif A[i1] <= A[i2] <= A[i3] or A[i3] <= A[i2] <= A[i1]:
        m = i2
    else:
        m = i3
    A[m], A[r] = A[r], A[m]
    return partition(A, p, r)
