from book.chapter6.section5 import max_heap_maximum
from book.data_structures import CT
from book.data_structures import KeyObject
from book.data_structures import PriorityQueue
from book.data_structures import T
from util import ceil_div


def multiary_parent(d: int, i: int) -> int:
    """The index of the parent of a multiary heap node.

    Implements:
        Multiary-Parent

    Args:
        d: the arity of the heap, d >= 2
        i: the index of the node

    Returns:
        The index of the parent of the node at index i in a d-ary heap.
    """
    return ceil_div(i - 1, d)


def multiary_child(d: int, i: int, k: int) -> int:
    """The index of a child of a multiary heap node.

    Implements:
        Multiary-Child

    Args:
        d: the arity of the heap, d >= 2
        i: the index of the node
        k: the number of a child to get, 1 <= k <= d

    Returns:
        The index of the k-th child of the node at index i in a d-ary heap.
    """
    return d * (i - 1) + k + 1


def multiary_max_heapify(A: PriorityQueue[CT], d: int, i: int) -> None:
    """Restores the max-heap property violated by a single multiary max-heap node.

    Implements:
        Multiary-Max-Heapify

    Args:
        A: the array representing the d-ary max-heap in which the max-heap property is violated by a single node
        d: the arity of the heap
        i: the index of the node in A that is not larger than either of its children
    """
    largest = i
    l = multiary_child(d, i, 1)
    j = 0
    while j < d and l + j <= A.heap_size:
        if A[l + j].key > A[largest].key:
            largest = l + j
        j += 1
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        multiary_max_heapify(A, d, largest)


def multiary_max_heap_extract_max(A: PriorityQueue[T], d: int) -> KeyObject[T]:
    """Removes and returns the element of the multiary max-heap with the largest key.

    Implements:
        Multiary-Max-Heap-Extract-Max

    Args:
        A: the array representing the d-ary max-heap
        d: the arity of the heap

    Returns:
        The element x removed from A such that x.key is the largest key among elements in A.
    """
    max = max_heap_maximum(A)
    A[1] = A[A.heap_size]
    A.heap_size -= 1
    multiary_max_heapify(A, d, 1)
    return max
