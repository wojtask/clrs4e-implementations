from book.data_structures import Array
from util import range_of


def merge(A: Array, p: int, q: int, r: int) -> None:
    """Merges two sorted subarrays to form a single sorted subarray in place.

    Implements pseudocode procedure Merge.

    Args:
        A: an Array containing the values to be
        p: the lower index of the first subarray to merge
        q: the upper index of the first subarray to merge
        r: the upper index of the second subarray to merge
    """
    nL = q - p + 1
    nR = r - q
    L = Array(0, nL - 1)
    R = Array(0, nR - 1)
    for i in range_of(0, to=nL - 1):
        L[i] = A[p + i]
    for j in range_of(0, to=nR - 1):
        R[j] = A[q + j + 1]
    i = 0
    j = 0
    k = p
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A: Array, p: int, r: int) -> None:
    """Reorders a sequence of values according to their "<=" relation.

    Implements pseudocode procedure Merge-Sort.

    Args:
        A: an Array containing the values to be sorted
        p: the lower index of the subarray to sort
        r: the upper index of the subarray to sort
    """
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)


def insertion_sort_with_binary_search(A: Array, n: int) -> None:
    """Reorders a sequence of values according to their "<=" relation.

    Args:
        A: an Array containing the values to be sorted
        n: the number of values to sort
    """
    for i in range_of(2, to=n):
        key = A[i]
        k = __binary_search_position(A, key, 1, i - 1)
        for j in range_of(i - 1, downto=k):
            A[j + 1] = A[j]
            j -= 1
        A[k] = key


def __binary_search_position(A: Array, x: int, p: int, r: int) -> int:
    if p > r:
        return p
    q = (p + r) // 2
    if x == A[q]:
        return q
    if x < A[q]:
        return __binary_search_position(A, x, p, q - 1)
    else:
        return __binary_search_position(A, x, q + 1, r)
