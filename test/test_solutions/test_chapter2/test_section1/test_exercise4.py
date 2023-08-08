from unittest import TestCase

from hamcrest import assert_that, is_
from hypothesis import given
from hypothesis.strategies import lists, integers

from array_util import create_array
from solutions.chapter2.section1.exercise4 import linear_search


class TestLinearSearch(TestCase):

    @given(lists(integers(min_value=-10, max_value=10), min_size=1, max_size=20),
           integers(min_value=-10, max_value=10))
    def test_linear_search(self, elements, x):
        A = create_array(elements)
        n = len(elements)

        actual_index = linear_search(A, n, x)

        if actual_index:
            assert_that(A[actual_index], is_(x))
        else:
            assert_that(x not in elements)
