import math

from book.chapter6.section1 import parent
from book.chapter6.section2 import max_heapify
from book.data_structures import KeyObject
from book.data_structures import PriorityQueue
from util import range_of


def max_heap_maximum(A: PriorityQueue) -> KeyObject:
    """Returns the element of the dynamic set with the largest key.

    Implements:
        Max-Heap-Maximum

    Args:
        A: a max-priority queue implemented by a max-heap containing elements of the dynamic set

    Returns:
        The element x from A such that x.key is the largest key among elements in A.
    """
    if A.heap_size < 1:
        raise ValueError('heap underflow')
    return A[1]


def max_heap_extract_max(A: PriorityQueue) -> KeyObject:
    """Removes and returns the element of the dynamic set with the largest key.

    Implements:
        Max-Heap-Extract-Max

    Args:
        A: a max-priority queue implemented by a max-heap containing elements of the dynamic set

    Returns:
        The element x removed from A such that x.key is the largest key among elements in A.
    """
    max = max_heap_maximum(A)
    A[1] = A[A.heap_size]
    A.heap_size -= 1
    max_heapify(A, 1)
    return max


def max_heap_increase_key(A: PriorityQueue, x: KeyObject, k: int) -> None:
    """Increases the value of the element's key to the new value.

    Implements:
        Max-Heap-Increase-Key

    Args:
        A: a max-priority queue implemented by a max-heap containing elements of the dynamic set
        x: an element in A whose key to increase
        k: a new value of the key, at least as large as x.key
    """
    if k < x.key:
        raise ValueError('new key is smaller than current key')
    x.key = k
    i = __find_index_of_object(A, x)
    while i > 1 and A[parent(i)].key < A[i].key:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def __find_index_of_object(A: PriorityQueue, x: KeyObject) -> int:
    for i in range_of(1, to=A.heap_size):
        if A[i] == x:
            return i
    raise ValueError('element not found in the heap')


def max_heap_insert(A: PriorityQueue, x: KeyObject, n: int) -> None:
    """Inserts a new element into the dynamic set.

    Implements:
        Max-Heap-Insert

    Args:
        A: a max-priority queue implemented by a max-heap containing elements of the dynamic set
        x: a new element to insert to A
        n: the number of elements in A
    """
    if A.heap_size == n:
        raise ValueError('heap overflow')
    A.heap_size += 1
    k = x.key
    x.key = -math.inf
    A[A.heap_size] = x
    max_heap_increase_key(A, x, k)
