from book.data_structures import Array
from book.chapter2.section3 import merge_sort
from solutions.chapter2.section3.exercise6 import binary_search
from util import range_of


def sum_search(A: Array, n: int, x: int) -> bool:
    merge_sort(A, 1, n)
    i = 1
    while i < n and A[i] < x / 2:
        if binary_search(A, x - A[i], i + 1, n) is not None:
            return True
        i += 1
    return False
