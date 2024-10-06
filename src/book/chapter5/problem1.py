from random import uniform

from book.data_structures import Array
from book.data_structures import Bit
from util import range_of


def increment(A: Array[Bit], b: int, count_sequence: Array[int]) -> None:
    """Increments the counter in a probabilistic manner, according to the count sequence.

    Implements:
        Increment
    """
    value = __compute_value(A, b)
    if value == 2 ** b - 1:
        raise ValueError('overflow')
    p = uniform(0, 1)
    if p <= 1 / (count_sequence[value + 1] - count_sequence[value]):
        __binary_counter_increment(A, b)


def __compute_value(A: Array[Bit], b: int) -> int:
    value = 0
    for i in range_of(0, to=b - 1):
        value += A[i] * 2 ** i
    return value


# TODO(#26) move to book.chapter16.section1
def __binary_counter_increment(A: Array[Bit], k: int) -> None:
    i = 0
    while i < k and A[i] == 1:
        A[i] = 0
        i += 1
    if i < k:
        A[i] = 1
