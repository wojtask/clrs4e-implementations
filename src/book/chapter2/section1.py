from book.data_structures import Array
from book.data_structures import CT
from util import range_of


def insertion_sort(A: Array[CT], n: int) -> None:
    """Sorts an array using insertion sort.

    Implements:
        Insertion-Sort

    Args:
        A: an Array containing the values to be sorted
        n: the number of values to sort
    """
    for i in range_of(2, to=n):
        key = A[i]
        j = i - 1
        while j > 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


def sum_array(A: Array[int], n: int) -> int:
    """Computes the sum of numbers in a sequence.

    Implements:
        Sum-Array

    Args:
        A: an Array containing the numbers to sum up
        n: the number of numbers to sum up

    Returns:
        The sum of the numbers in A[1:n].
    """
    sum = 0
    for i in range_of(1, to=n):
        sum += A[i]
    return sum
