from hypothesis import assume
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from solutions.chapter5.section1.exercise2 import random
from solutions.chapter5.section1.exercise3 import unbiased_random
from solutions.chapter5.section3.exercise1 import randomly_permute_
from test_case import ClrsTestCase
from test_util import create_array
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

    @given(st.data())
    def test_randomly_permute_(self, data):
        elements = data.draw(lists(integers(), min_size=1, unique=True))
        A = create_array(elements)
        n = len(elements)

        randomly_permute_(A, n)

        self.assertArrayPermuted(A, elements, end=n)
