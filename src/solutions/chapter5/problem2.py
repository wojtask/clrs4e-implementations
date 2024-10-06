from __future__ import annotations

from book.data_structures import Array
from book.data_structures import T
from solutions.chapter5.section1.exercise2 import random
from util import range_of


def random_search(A: Array[T], n: int, x: T) -> int | None:
    """Searches for an element in a sequence of elements by randomly choosing next element to check.

    Implements:
        Random-Search

    Args:
        A: an Array containing the sequence of elements
        n: the number of elements in the sequence
        x: the element to search for

    Returns:
        An index i such that x equals A[i] or None if x does not appear in A.
    """
    picked = Array[bool](1, n)
    for i in range_of(1, to=n):
        picked[i] = False
    k = 0
    while k < n:
        i = random(1, n)
        if A[i] == x:
            return i
        if not picked[i]:
            picked[i] = True
            k += 1
    return None
