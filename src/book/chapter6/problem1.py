from book.chapter6.section5 import max_heap_insert
from book.data_structures import Heap
from book.data_structures import Record
from book.data_structures import T
from util import range_of


def build_max_heap_(A: Heap[Record[T]], n: int) -> None:
    """Converts an array into a max-heap by repeatedly inserting elements to the heap.

    Implements:
        Build-Max-Heap'

    Args:
        A: the array data structure for heap representation
        n: the number of elements in A
    """
    A.heap_size = 1
    for i in range_of(2, to=n):
        max_heap_insert(A, A[i], n)
