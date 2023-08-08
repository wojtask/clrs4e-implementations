from unittest import TestCase

from hamcrest import assert_that, is_
from hypothesis import given
from hypothesis.strategies import lists, integers

from array_util import create_array
from solutions.chapter2.section3.exercise8 import sum_search


class TestSumSearch(TestCase):

    @given(lists(integers(min_value=-10, max_value=10), min_size=1, unique=True),
           integers(min_value=-20, max_value=20))
    def test_sum_search_positive(self, elements, x):
        A = create_array(elements)
        n = len(elements)

        actual_found = sum_search(A, n, x)

        all_sums = {a + b for a in elements for b in elements if a != b}
        expected_found = x in all_sums
        assert_that(actual_found, is_(expected_found))
