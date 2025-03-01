from book.chapter6.section2 import max_heapify
from book.data_structures import KeyObject
from book.data_structures import PriorityQueue
from solutions.chapter2.section1.exercise4 import linear_search


def max_heap_decrease_key(A: PriorityQueue, x: KeyObject, k: int) -> None:
    """Increases the value of the element's key to the new value.

    Implements:
        Max-Heap-Decrease-Key

    Args:
        A: a max-priority queue implemented by a max-heap containing elements of the dynamic set
        x: an element in A whose key to decrease
        k: a new value of the key, at most as large as x.key
    """
    if k > x.key:
        raise ValueError('new key is larger than current key')
    x.key = k
    i = __find_index_of_object(A, x)
    max_heapify(A, i)


def __find_index_of_object(A: PriorityQueue, x: KeyObject) -> int:
    return linear_search(A, A.heap_size, x)
