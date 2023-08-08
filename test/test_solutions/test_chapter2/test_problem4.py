from unittest import TestCase

from hamcrest import assert_that, is_
from hypothesis import given
from hypothesis.strategies import lists, integers

from array_util import create_array
from solutions.chapter2.problem4 import count_inversions
from util import range_of


def get_inversions(elements):
    A = create_array(elements)
    n = len(elements)
    inversions = 0
    for i in range_of(1, to=n-1):
        for j in range_of(i + 1, to=n):
            if A[i] > A[j]:
                inversions += 1
    return inversions


class TestCountInversions(TestCase):

    @given(lists(integers(), min_size=1))
    def test_count_inversions(self, elements):
        A = create_array(elements)
        n = len(elements)

        actual_inversions = count_inversions(A, 1, n)

        # expected_inversions = sum(
        #     len([y for y in elements[i + 1:] if y < x]) for i, x in enumerate(elements, start=1))
        expected_inversions = get_inversions(elements)
        assert_that(actual_inversions, is_(expected_inversions))
