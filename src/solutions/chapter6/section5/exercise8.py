from book.chapter6.section1 import parent
from book.data_structures import PriorityQueue
from book.data_structures import Record
from book.data_structures import T


def max_heap_increase_key_(A: PriorityQueue[T], x: Record[T], k: float) -> None:
    """Increases the value of the element's key to the new value. This version of the procedure uses fewer object
    assignments than the original Max-Heap-Insert-Key.

    Implements:
        Max-Heap-Increase-Key_

    Args:
        A: a max-priority queue implemented by a max-heap containing elements of the dynamic set
        x: an element in A whose key to increase
        k: a new value of the key, at least as large as x.key
    """
    if k < x.key:
        raise ValueError('new key is smaller than current key')
    x.key = k
    i = __find_index_of_object(A, x)
    while i > 1 and A[parent(i)].key < k:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = x


def __find_index_of_object(A: PriorityQueue[T], x: Record[T]) -> int:
    return A.mapping[x]
