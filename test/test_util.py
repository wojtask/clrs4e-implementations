from typing import Union

from book.data_structures import Array
from book.data_structures import Matrix
from util import range_of


def create_array(elements: list, start: int = 1) -> Array:
    n = len(elements)
    array = Array(start, n + start - 1)
    i = start
    for e in elements:
        array[i] = e
        i += 1
    return array


def create_matrix(elements: list[list[Union[int, float]]]) -> Matrix:
    rows = len(elements)
    cols = len(elements[0])
    matrix = Matrix(rows, cols)
    for row in range_of(1, to=rows):
        for col in range_of(1, to=cols):
            matrix[row, col] = elements[row - 1][col - 1]
    return matrix


def binary_to_decimal(A: Array, n: int) -> int:
    result = 0
    for i in range_of(0, to=n - 1):
        result += A[i] * 2 ** i
    return result
