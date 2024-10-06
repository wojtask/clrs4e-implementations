import math

from book.data_structures import Array
from util import range_of


# Added the implicit score array to the list of parameters
def online_maximum(score: Array[int], k: int, n: int) -> int:
    """An online version of the algorithm to find the best candidate.

    Implements:
        Online-Maximum

    Args:
        score: the distinct scores of the candidates
        k: the number of candidates to reject at first, before hiring the next better qualified one
        n: the number of candidates

    Returns:
        The position of the first applicant after the first k, that has higher score than all preceding applicants,
        or n if the best-qualified applicant was among the first k interviewed.
    """
    best_score = -math.inf
    for i in range_of(1, to=k):
        if score[i] > best_score:
            best_score = score[i]
    for i in range_of(k + 1, to=n):
        if score[i] > best_score:
            return i
    return n
