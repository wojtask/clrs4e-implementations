from book.data_structures import Array
from util import range_of


def insertion_sort(A: Array, n: int) -> None:
    """Reorders a sequence of values according to their "<=" relation.

    Implements pseudocode procedure Insertion-Sort from Section 2.1 of the book.

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


def sum_array(A: Array, n: int) -> int:
    """Computes the sum of numbers in a sequence.

    Implements pseudocode procedure Sum-Array from Section 2.1 of the book.

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
