import math

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import just
from hypothesis.strategies import lists

from solutions.chapter7.section1.exercise2 import fair_partition
from test_case import ClrsTestCase
from test_util import create_array
from util import range_of


class TestChapter7(ClrsTestCase):

    @given(st.data())
    def test_fair_partition(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        actual_split_index = fair_partition(A, 1, n)

        left_max = -math.inf
        right_min = math.inf
        for i in range_of(1, to=actual_split_index):
            left_max = max(left_max, A[i])
        for i in range_of(actual_split_index + 1, to=n):
            right_min = min(right_min, A[i])
        self.assertLessEqual(left_max, right_min)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_fair_partition_all_values_equal(self, data):
        value = data.draw(integers())
        elements = data.draw(lists(just(value), min_size=1))
        A = create_array(elements)
        n = len(elements)

        actual_split_index = fair_partition(A, 1, n)

        self.assertEqual(actual_split_index, (n + 1) // 2)
