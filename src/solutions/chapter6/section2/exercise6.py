from book.chapter6.section1 import left
from book.chapter6.section1 import right
from book.data_structures import CT
from book.data_structures import Heap


def iterative_max_heapify(A: Heap[CT], i: int) -> None:
    """Restores the max-heap property violated by a single node (an iterative version).

    Implements:
        Iterative-Max-Heapify

    Args:
        A: the array representing a max-heap in which the max-heap property is violated by a single node
        i: the index of the node in A that is not larger than either of its children
    """
    while True:
        l = left(i)
        r = right(i)
        if l <= A.heap_size and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r <= A.heap_size and A[r] > A[largest]:
            largest = r
        if largest == i:
            return
        A[i], A[largest] = A[largest], A[i]
        i = largest
