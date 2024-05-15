from typing import Optional

from book.data_structures import Array
from solutions.chapter5.section1.exercise2 import random
from util import range_of


def random_search(A: Array, n: int, x: int) -> Optional[int]:
    """Searches for a number in a sequence of numbers by randomly choosing subsequent numbers to check.

    Implements:
        Random-Search

    Args:
        A: an Array containing the sequence of numbers
        n: the number of numbers in the sequence
        x: the number to search for

    Returns:
        An index i such that x equals A[i] or None if x does not appear in A.
    """
    picked = Array(1, n)
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
