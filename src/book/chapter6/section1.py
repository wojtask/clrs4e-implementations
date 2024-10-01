from util import range_of


def parent(i: int) -> int:
    """The index of the parent of a heap node.

    Implements:
        Parent

    Args:
        i: the index of the node

    Returns:
        The index of the parent of the node at index i.
    """
    return i // 2


def left(i: int) -> int:
    """The index of the left child of a heap node.

    Implements:
        Left

    Args:
        i: the index of the node

    Returns:
        The index of the left child of the node at index i.
    """
    return 2 * i


def right(i: int) -> int:
    """The index of the right child of a heap node.

    Implements:
        Right

    Args:
        i: the index of the node

    Returns:
        The index of the right child of the node at index i.
    """
    return 2 * i + 1


def max_heapify(A, i: int) -> None:
    """Restores the max-heap property violated by a single node.

    Implements:
        Max-Heapify

    Args:
        A: the array representing a max-heap in which the max-heap property is violated by a single node
        i: the index of the node in A that is not larger than either of its children
    """
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


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
