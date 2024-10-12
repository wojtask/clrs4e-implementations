from book.chapter6.section2 import max_heapify
from book.chapter6.section3 import build_max_heap
from book.data_structures import CT
from book.data_structures import Heap
from util import range_of


def heapsort(A: Heap[CT], n: int) -> None:
    """Sorts an array using heapsort.

    Implements:
        Heapsort

    Args:
        A: an array capable of representing a heap, containing the values to be sorted
        n: the number of values to sort
    """
    build_max_heap(A, n)
    for i in range_of(n, downto=2):
        A[1], A[i] = A[i], A[1]
        A.heap_size -= 1
        max_heapify(A, 1)
