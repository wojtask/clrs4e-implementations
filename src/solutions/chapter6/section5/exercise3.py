import math

from book.chapter6.section1 import parent
from book.data_structures import KeyObject
from book.data_structures import PriorityQueue
from solutions.chapter2.section1.exercise4 import linear_search
from solutions.chapter6.section2.exercise3 import min_heapify


def min_heap_minimum(A: PriorityQueue) -> KeyObject:
    """Returns the element of the dynamic set with the smallest key.

    Implements:
        Min-Heap-Minimum

    Args:
        A: a min-priority queue implemented by a min-heap containing elements of the dynamic set

    Returns:
        The element x from A such that x.key is the smallest key among elements in A.
    """
    if A.heap_size < 1:
        raise ValueError('heap underflow')
    return A[1]


def min_heap_extract_min(A: PriorityQueue) -> KeyObject:
    """Removes and returns the element of the dynamic set with the smallest key.

    Implements:
        Min-Heap-Extract-Min

    Args:
        A: a min-priority queue implemented by a min-heap containing elements of the dynamic set

    Returns:
        The element x removed from A such that x.key is the smallest key among elements in A.
    """
    min = min_heap_minimum(A)
    A[1] = A[A.heap_size]
    A.heap_size -= 1
    min_heapify(A, 1)
    return min


def min_heap_decrease_key(A: PriorityQueue, x: KeyObject, k: int) -> None:
    """Decreases the value of the element's key to the new value.

    Implements:
        Min-Heap-Decrease-Key

    Args:
        A: a min-priority queue implemented by a min-heap containing elements of the dynamic set
        x: an element in A whose key to decrease
        k: a new value of the key, at most as large as x.key
    """
    if k > x.key:
        raise ValueError('new key is larger than current key')
    x.key = k
    i = __find_index_of_object(A, x)
    while i > 1 and A[parent(i)].key > A[i].key:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def __find_index_of_object(A: PriorityQueue, x: KeyObject) -> int:
    return linear_search(A, A.heap_size, x)


def min_heap_insert(A: PriorityQueue, x: KeyObject, n: int) -> None:
    """Inserts a new element into the dynamic set.

    Implements:
        Min-Heap-Insert

    Args:
        A: a min-priority queue implemented by a min-heap containing elements of the dynamic set
        x: a new element to insert to A
        n: the number of elements in A
    """
    if A.heap_size == n:
        raise ValueError('heap overflow')
    A.heap_size += 1
    k = x.key
    x.key = math.inf
    A[A.heap_size] = x
    min_heap_decrease_key(A, x, k)
