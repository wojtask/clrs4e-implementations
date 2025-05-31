from book.chapter7.section1 import partition
from book.data_structures import Array
from book.data_structures import CT


def tre_quicksort(A: Array[CT], p: int, r: int) -> None:
    """Sorts an array using quicksort with tail-recursion elimination.

    Implements:
        TRE-Quicksort

    Args:
        A: an Array containing the values to be sorted
        p: the lower index of the subarray to sort
        r: the upper index of the subarray to sort
    """
    while p < r:
        q = partition(A, p, r)
        tre_quicksort(A, p, q - 1)
        p = q + 1
