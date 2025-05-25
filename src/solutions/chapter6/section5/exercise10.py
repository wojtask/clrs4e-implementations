import math

from book.chapter6.section5 import max_heap_extract_max
from book.chapter6.section5 import max_heap_increase_key
from book.data_structures import KeyObject
from book.data_structures import PriorityQueue
from book.data_structures import T


def max_heap_delete(A: PriorityQueue[T], x: KeyObject[T]) -> None:
    """Deletes an element from a max-heap.

    Implements:
        Max-Heap-Delete

    Args:
        A: the array representing a max-heap
        x: the element of the max-heap in A to delete
    """
    max_heap_increase_key(A, x, math.inf)
    max_heap_extract_max(A)
