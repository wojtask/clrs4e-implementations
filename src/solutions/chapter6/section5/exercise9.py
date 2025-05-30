from book.chapter6.section5 import max_heap_extract_max
from book.chapter6.section5 import max_heap_insert
from book.data_structures import PriorityQueue
from book.data_structures import Record
from book.data_structures import T
from solutions.chapter6.section5.exercise3 import min_heap_extract_min
from solutions.chapter6.section5.exercise3 import min_heap_insert


class ControlledPriorityQueue(PriorityQueue[T]):
    priority: int = 1


def min_heap_enqueue(A: ControlledPriorityQueue[T], x: Record[T], n: int) -> None:
    """Inserts an element into a first-in, first-out queue implemented with a priority queue.

    Implements:
        Min-Heap-Enqueue

    Args:
        A: the min-priority queue implemented with a min-heap
        x: the element to insert into the queue
        n: the capacity of A
    """
    x.key = A.priority
    min_heap_insert(A, x, n)
    A.priority += 1


def min_heap_dequeue(A: ControlledPriorityQueue[T]) -> Record[T]:
    """Deletes an element from a first-in, first-out queue implemented with a priority queue.

    Implements:
        Min-Heap-Dequeue

    Args:
        A: the min-priority queue implemented with a min-heap

    Returns:
        The element that has been in A for the longest time, deleted from A.
    """
    return min_heap_extract_min(A)


def max_heap_push(A: ControlledPriorityQueue[T], x: Record[T], n: int) -> None:
    """Inserts an element into a stack implemented with a priority queue.

    Implements:
        Max-Heap-Push

    Args:
        A: the max-priority queue implemented with a max-heap
        x: the element to insert into the stack
        n: the capacity of A
    """
    x.key = A.priority
    max_heap_insert(A, x, n)
    A.priority += 1


def max_heap_pop(A: ControlledPriorityQueue[T]) -> Record[T]:
    """Deletes an element from a stack implemented with a priority queue.

    Implements:
        Max-Heap-Pop

    Args:
        A: the max-priority queue implemented with a max-heap

    Returns:
        The element that has been in A for the shortest time, deleted from A.
    """
    return max_heap_extract_max(A)
