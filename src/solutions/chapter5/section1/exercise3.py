from typing import Literal

from book.chapter5.section1 import biased_random


def unbiased_random() -> Literal[0, 1]:
    """Outputs unbiased answer, either 0 or 1, using Biased-Random as a subroutine.

    Implements:
        Unbiased-Random

    Returns: 0 with probability 1/2 and 1 with probability 1/2.
    """
    while True:
        x = biased_random()
        y = biased_random()
        if x != y:
            break
    return x
