from book.chapter2.section3 import merge
from book.data_structures import Array
from book.data_structures import CT
from util import range_of


def merge_sort_with_insertion_sort(A: Array[CT], p: int, r: int, k: int) -> None:
    """Sorts an array using merge sort, while delegating small subproblems to insertion sort.

    Args:
        A: an Array containing the values to be sorted
        p: the lower index of the subarray to sort
        r: the upper index of the subarray to sort
        k: the subarray length threshold; subarrays up to this length are sorted using insertion sort
    """
    if p >= r:
        return
    if r - p + 1 <= k:
        __insertion_sort_sublist(A, p, r)
    q = (p + r) // 2
    merge_sort_with_insertion_sort(A, p, q, k)
    merge_sort_with_insertion_sort(A, q + 1, r, k)
    merge(A, p, q, r)


def __insertion_sort_sublist(A: Array[CT], p: int, r: int) -> None:
    for i in range_of(p + 1, to=r):
        key = A[i]
        j = i - 1
        while j >= p and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
