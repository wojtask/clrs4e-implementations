from book.data_structures import Array
from book.data_structures import Matrix
from util import range_of


def create_array(elements, start=1):
    n = len(elements)
    array = Array(start, n + start - 1)
    i = start
    for e in elements:
        array[i] = e
        i += 1
    return array


def create_matrix(elements):
    rows = len(elements)
    cols = len(elements[0])
    matrix = Matrix(rows, cols)
    for row in range_of(1, to=rows):
        for col in range_of(1, to=cols):
            matrix[row, col] = elements[row - 1][col - 1]
    return matrix
