from book.chapter6.section2 import max_heapify
from util import range_of


def build_max_heap(A, n: int) -> None:
    """Converts an array into a max-heap.

    Implements:
        Build-Max-Heap

    Args:
        A: the array
        n: the number of elements in A
    """
    A.heap_size = n
    for i in range_of(n // 2, downto=1):
        max_heapify(A, i)
