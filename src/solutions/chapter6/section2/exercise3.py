from book.chapter6.section1 import left
from book.chapter6.section1 import right


def min_heapify(A, i: int) -> None:
    """Restores the min-heap property violated by a single node.

    Implements:
        Min-Heapify

    Args:
        A: the array representing a min-heap in which the min-heap property is violated by a single node
        i: the index of the node in A that is not smaller than either of its children
    """
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= A.heap_size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)
