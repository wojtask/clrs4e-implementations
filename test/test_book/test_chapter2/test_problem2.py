from unittest import TestCase

from hamcrest import assert_that
from hypothesis import given
from hypothesis.strategies import lists, integers

from array_util import create_array, is_sorted, is_permutation
from book.chapter2.problem2 import bubblesort


class TestBubblesort(TestCase):

    @given(lists(integers(), min_size=1))
    def test_bubblesort(self, elements):
        A = create_array(elements)
        n = len(elements)

        bubblesort(A, n)

        assert_that(is_sorted(A, end=n))
        assert_that(is_permutation(A, elements, end=n))
