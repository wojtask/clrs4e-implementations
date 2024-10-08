from book.data_structures import Array
from book.data_structures import CT
from util import range_of


def bubblesort(A: Array[CT], n: int) -> None:
    """Sorts an array using bubblesort.

    Implements:
        Bubblesort

    Args:
        A: an Array containing the values to be sorted
        n: the number of values to sort
    """
    for i in range_of(1, to=n - 1):
        for j in range_of(n, downto=i + 1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
