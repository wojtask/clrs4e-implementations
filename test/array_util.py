import operator

from book.data_structures import Array
from util import range_of


def create_array(elements, start=1):
    n = len(elements)
    array = Array(start, n + start - 1)
    i = start
    for e in elements:
        array[i] = e
        i += 1
    return array


def is_sorted(array, start=1, end=None, cmp=operator.le):
    if start >= end:
        return True
    for i in range_of(start, to=end - 1):
        if not cmp(array[i], array[i + 1]):
            return False
    return True


def is_permutation(array, elements, start=1, end=None):
    if end - start + 1 != len(elements):
        return False
    for i in range_of(start, to=end):
        if array[i] not in elements:
            return False
    for e in elements:
        match = False
        for i in range_of(start, to=end):
            if array[i] == e:
                match = True
                break
        if not match:
            return False
    return True
