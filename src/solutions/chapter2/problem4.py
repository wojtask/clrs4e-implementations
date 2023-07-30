from book.data_structures import Array
from util import range_of


def merge_inversions(A: Array, p: int, q: int, r: int) -> int:
    """Merges two sorted subarrays to form a single sorted subarray in place, and counts inversions.

    Args:
        A: an Array with subarrays to be merged and inversions to count
        p: the lower index of the first sorted subarray
        q: the upper index of the first sorted subarray
        r: the upper index of the second sorted subarray

    Returns:
        The number of inversions contributed by elements originally in A[p:q] with elements originally in A[q+1:r].
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
    inversions = 0
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inversions += nL - i
        k += 1
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1
    return inversions


def count_inversions(A: Array, p: int, r: int) -> int:
    """Counts inversions in an array. Sorts the input array as a side effect.

    Implements pseudocode procedure Count-Inversions.

    Args:
        A: an Array with inversions to count
        p: the lower index of the subarray to sort
        r: the upper index of the subarray to sort

    Returns:
        The number of inversions originally in A[p:r].
    """
    inversions = 0
    if p < r:
        q = (p + r) // 2
        inversions += count_inversions(A, p, q)
        inversions += count_inversions(A, q + 1, r)
        inversions += merge_inversions(A, p, q, r)
    return inversions
