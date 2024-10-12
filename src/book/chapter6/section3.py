from book.chapter6.section2 import max_heapify
from book.data_structures import CT
from book.data_structures import Heap
from util import range_of


def build_max_heap(A: Heap[CT], n: int) -> None:
    """Converts an array into a max-heap.

    Implements:
        Build-Max-Heap

    Args:
        A: the array data structure for heap representation
        n: the number of elements in A
    """
    A.heap_size = n
    for i in range_of(n // 2, downto=1):
        max_heapify(A, i)
