from io import StringIO
from random import shuffle
from unittest.mock import patch

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from book.chapter5.section1 import hire_assistant
from book.chapter5.section3 import permute_by_cycle
from book.chapter5.section3 import permute_with_all
from book.chapter5.section3 import permute_without_identity
from book.chapter5.section3 import randomized_hire_assistant
from book.chapter5.section3 import randomly_permute
from test_case import ClrsTestCase
from test_util import create_array
from util import range_of


class TestChapter5(ClrsTestCase):

    @given(st.data())
    def test_hire_assistant(self, data):
        n = data.draw(st.integers(min_value=1, max_value=10))
        rank_elements = list(range_of(1, to=n))
        shuffle(rank_elements)
        rank = create_array(rank_elements)
        INTERVIEWING_PREFIX = 'interviewing candidate '
        HIRING_PREFIX = 'hiring candidate '

        with patch('sys.stdout', new=StringIO()) as fake_out:
            hire_assistant(rank, n)

            actual_output = fake_out.getvalue().splitlines()
            interviewed_candidates = [int(line.removeprefix(INTERVIEWING_PREFIX)) for line in actual_output if
                                      line.startswith(INTERVIEWING_PREFIX)]
            hired_candidates = [int(line.removeprefix(HIRING_PREFIX)) for line in actual_output if
                                line.startswith(HIRING_PREFIX)]
            self.assertEqual(len(interviewed_candidates), n)
            self.assertIn(len(hired_candidates), range_of(1, to=n))
            self.assertEqual(interviewed_candidates, list(range_of(1, to=n)))
            self.assertEqual(hired_candidates, sorted(hired_candidates))
            self.assertTrue(set(hired_candidates).issubset(set(interviewed_candidates)))

    @given(st.data())
    def test_randomized_hire_assistant(self, data):
        n = data.draw(st.integers(min_value=1, max_value=10))
        rank_elements = list(range_of(1, to=n))
        shuffle(rank_elements)
        rank = create_array(rank_elements)
        INTERVIEWING_PREFIX = 'interviewing candidate '
        HIRING_PREFIX = 'hiring candidate '

        with patch('sys.stdout', new=StringIO()) as fake_out:
            randomized_hire_assistant(rank, n)

            actual_output = fake_out.getvalue().splitlines()
            interviewed_candidates = [int(line.removeprefix(INTERVIEWING_PREFIX)) for line in actual_output if
                                      line.startswith(INTERVIEWING_PREFIX)]
            hired_candidates = [int(line.removeprefix(HIRING_PREFIX)) for line in actual_output if
                                line.startswith(HIRING_PREFIX)]
            self.assertEqual(len(interviewed_candidates), n)
            self.assertIn(len(hired_candidates), range_of(1, to=n))
            self.assertEqual(interviewed_candidates, list(range_of(1, to=n)))
            self.assertEqual(hired_candidates, sorted(hired_candidates))
            self.assertTrue(set(hired_candidates).issubset(set(interviewed_candidates)))

    @given(st.data())
    def test_randomly_permute(self, data):
        elements = data.draw(lists(integers(), min_size=3, max_size=3, unique=True))
        A = create_array(elements)
        n = len(elements)

        randomly_permute(A, n)

        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_permute_without_identity(self, data):
        elements = data.draw(lists(integers(), min_size=1, unique=True))
        A = create_array(elements)
        n = len(elements)

        permute_without_identity(A, n)

        self.assertArrayPermuted(A, elements, end=n)
        if n > 1:
            for i in range_of(1, to=n):
                self.assertNotEqual(A[i], elements[i - 1])

    @given(st.data())
    def test_permute_with_all(self, data):
        elements = data.draw(lists(integers(), min_size=1, unique=True))
        A = create_array(elements)
        n = len(elements)

        permute_with_all(A, n)

        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_permute_by_cycle(self, data):
        elements = data.draw(lists(integers(), min_size=1, unique=True))
        A = create_array(elements)
        n = len(elements)

        actual_permuted = permute_by_cycle(A, n)

        self.assertArrayPermuted(actual_permuted, elements, end=n)
        if n > 2:
            reversed_array = create_array(list(reversed(elements)))
            self.assertNotEqual(actual_permuted, reversed_array)
