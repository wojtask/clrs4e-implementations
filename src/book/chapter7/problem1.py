from book.data_structures import Array
from book.data_structures import CT


def hoare_partition(A: Array[CT], p: int, r: int) -> int:
    """Partitions an array into two subarrays, the low side and the high side, such that each element in the low side of
    the partition is less than or equal to each element in the high side. Uses the original algorithm invented by
    C. A. R. Hoare.

    Implements:
        Hoare-Partition

    Args:
        A: an Array to partition
        p: the lower index of the subarray to partition
        r: the upper index of the subarray to partition

    Returns:
        The index j such that each element in A[p:j] is less than or equal to each element in A[j + 1:r].
    """
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j -= 1
            if A[j] <= x:
                break
        while True:
            i += 1
            if A[i] >= x:
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j
