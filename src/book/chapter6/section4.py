from book.chapter6.section2 import max_heapify
from book.chapter6.section3 import build_max_heap
from util import range_of


def heapsort(A, n: int) -> None:
    """Sorts an array using heapsort.

    Implements:
        Heapsort

    Args:
        A: an Array containing the values to be sorted
        n: the number of values to sort
    """
    build_max_heap(A, n)
    for i in range_of(n, downto=2):
        A[1], A[i] = A[i], A[1]
        A.heap_size -= 1
        max_heapify(A, 1)
