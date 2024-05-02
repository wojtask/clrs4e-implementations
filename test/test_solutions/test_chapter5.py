from hypothesis import assume
from hypothesis import given
from hypothesis import strategies as st

from solutions.chapter5.section1.exercise2 import random
from solutions.chapter5.section1.exercise3 import unbiased_random
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

    def test_unbiased_random(self):
        samples = 1000
        count0 = 0
        for _ in range_of(1, to=samples):

            x = unbiased_random()

            self.assertIn(x, range_of(0, to=1))
            if x == 0:
                count0 += 1
        self.assertAlmostEqual(count0 / samples, 0.5, delta=0.1)
