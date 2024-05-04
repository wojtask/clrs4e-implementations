from book.chapter5.section1 import hire_assistant
from book.data_structures import Array
from solutions.chapter5.section1.exercise2 import random
from util import range_of


def randomized_hire_assistant(rank: Array, n: int) -> None:
    """Randomized version of Hire-Assistant.

    Implements:
        Randomized-Hire-Assistant

    Args:
        rank: the ranks of the candidates (a permutation of {1, 2, ..., n})
        n: the number of candidates
    """
    randomly_permute(rank, n)
    hire_assistant(rank, n)


def randomly_permute(A: Array, n: int) -> None:
    """Permutes an array in place, producing a uniform random permutation.

    Implements:
        Randomly-Permute

    Args:
        A: the array to permute
        n: the number of elements in array A
    """
    for i in range_of(1, to=n):
        # if we used two calls to Random(i, n) in the swap instruction, each call might generate a different value
        j = random(i, n)
        A[i], A[j] = A[j], A[i]


def permute_without_identity(A: Array, n: int) -> None:
    """A deliberately faulty algorithm for producing any permutation of an array without the identity permutation.
    Fails to produce any permutation in which an element on a given position occupied the same position in the original
    array.

    Implements:
        Permute-Without-Identity

    Args:
        A: the array to permute
        n: the number of elements in array A
    """
    for i in range_of(1, to=n - 1):
        # if we used two calls to Random(i + 1, n) in the swap instruction, each call might generate a different value
        j = random(i + 1, n)
        A[i], A[j] = A[j], A[i]


def permute_with_all(A: Array, n: int) -> None:
    """Permutes an array in place. Can't produce a uniform random permutation.

    Implements:
        Permute-With-All

    Args:
        A: the array to permute
        n: the number of elements in array A
    """
    for i in range_of(1, to=n):
        # if we used two calls to Random(1, n) in the swap instruction, each call might generate a different value
        j = random(1, n)
        A[i], A[j] = A[j], A[i]
