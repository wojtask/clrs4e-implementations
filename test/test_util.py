from __future__ import annotations

from book.data_structures import Array
from book.data_structures import Bit
from book.data_structures import CT
from book.data_structures import Heap
from book.data_structures import KeyObject
from book.data_structures import Matrix
from book.data_structures import PriorityQueue
from book.data_structures import T
from util import range_of


def create_array(elements: list[T], start: int = 1) -> Array[T]:
    n = len(elements)
    array = Array[T](start, n + start - 1)
    i = start
    for e in elements:
        array[i] = e
        i += 1
    return array


def create_matrix(elements: list[list[float]]) -> Matrix:
    rows = len(elements)
    cols = len(elements[0])
    matrix = Matrix(rows, cols)
    for row in range_of(1, to=rows):
        for col in range_of(1, to=cols):
            matrix[row, col] = elements[row - 1][col - 1]
    return matrix


def create_heap(elements: list[CT], capacity: int | None = None) -> Heap[CT]:
    heap = Heap[CT](1, capacity if capacity else len(elements))
    heap.heap_size = len(elements)
    for i in range_of(1, to=len(elements)):
        heap[i] = elements[i - 1]
    return heap


def create_priority_queue(heap: Heap[KeyObject[T]], capacity: int | None = None) -> PriorityQueue[T]:
    priority_queue = PriorityQueue[T](capacity if capacity else heap.heap_size)
    priority_queue.heap_size = heap.heap_size
    for i in range_of(1, to=heap.heap_size):
        priority_queue[i] = heap[i]
    return priority_queue


def binary_to_decimal(A: Array[Bit], n: int) -> int:
    result = 0
    for i in range_of(0, to=n - 1):
        result += A[i] * 2 ** i
    return result
