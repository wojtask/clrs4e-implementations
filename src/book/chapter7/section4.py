from book.chapter7.section1 import partition
from book.data_structures import Array
from book.data_structures import CT
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
