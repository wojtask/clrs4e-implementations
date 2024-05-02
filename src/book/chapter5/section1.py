import random

from util import range_of


rank = []


def hire_assistant(n: int) -> None:
    """Interviews a set of candidates and hires the best qualified one as an office assistant.

    Args:
        n: the number of candidates
    """
    # ADDED: initialize the ranks of the candidates to a permutation of {1, 2, ..., n} (plus 0 for the dummy)
    __init_ranks(n)
    best = 0
    for i in range_of(1, to=n):
        __interview_candidate(i)
        if __compare_candidates(i, best):
            best = i
            __hire_candidate(i)


def __init_ranks(n):
    global rank
    rank = list(range_of(0, to=n))
    random.shuffle(rank[1:])


def __interview_candidate(i):
    print('interviewing candidate ' + str(i))


def __compare_candidates(i, j):
    global rank
    return rank[i] > rank[j]


def __hire_candidate(i):
    print('hiring candidate ' + str(i))
