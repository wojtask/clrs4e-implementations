from book.data_structures import Array


def recursive_insertion_sort(A: Array, n: int) -> None:
    """Sorts an array using a recursive version of insertion sort.

    Implements:
        Recursive-Insertion-Sort

    Args:
        A: an Array containing the values to be sorted
        n: the number of values to sort
    """
    if n > 1:
        recursive_insertion_sort(A, n - 1)
    key = A[n]
    j = n - 1
    while j > 0 and A[j] > key:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key
