from hypothesis import assume
from hypothesis import given
from hypothesis import strategies as st

from solutions.chapter5.section1.exercise2 import random
from test_case import ClrsTestCase
from util import range_of


class TestChapter5(ClrsTestCase):

    @given(st.data())
    def test_random(self, data):
        a = data.draw(st.integers(min_value=1, max_value=100))
        b = data.draw(st.integers(min_value=1, max_value=100))
        assume(a <= b)

        x = random(a, b)

        self.assertIn(x, range_of(a, to=b))
