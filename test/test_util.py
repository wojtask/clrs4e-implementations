from __future__ import annotations

from book.data_structures import Array
from book.data_structures import Bit
from book.data_structures import CT
from book.data_structures import Heap
from book.data_structures import Matrix
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


def create_matrix(elements: list[list[int]]) -> Matrix:
    rows = len(elements)
    cols = len(elements[0])
    matrix = Matrix(rows, cols)
    for row in range_of(1, to=rows):
        for col in range_of(1, to=cols):
            matrix[row, col] = elements[row - 1][col - 1]
    return matrix


def create_heap(elements: list[CT]) -> Heap[CT]:
    n = len(elements)
    heap = Heap[CT](1, n)
    for i in range_of(1, n):
        heap[i] = elements[i - 1]
    heap.heap_size = n
    return heap


def binary_to_decimal(A: Array[Bit], n: int) -> int:
    result = 0
    for i in range_of(0, to=n - 1):
        result += A[i] * 2 ** i
    return result
