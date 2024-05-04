from book.data_structures import Array
from util import range_of


# Added the implicit rank array to the list of parameters
def hire_assistant(rank: Array, n: int) -> None:
    """Interviews a set of candidates and hires the best qualified one as an office assistant.

    Implements:
        Hire-Assistant

    Args:
        rank: the ranks of the candidates (a permutation of {1, 2, ..., n})
        n: the number of candidates
    """
    best = 0
    for i in range_of(1, to=n):
        __interview_candidate(i)
        if __compare_candidates(i, best, rank):
            best = i
            __hire_candidate(i)


def __interview_candidate(i):
    print('interviewing candidate ' + str(i))


def __compare_candidates(i, j, rank):
    return j == 0 or rank[i] > rank[j]


def __hire_candidate(i):
    print('hiring candidate ' + str(i))
