from io import StringIO
from unittest.mock import patch

from hypothesis import given
from hypothesis import strategies as st

from book.chapter5.section1 import hire_assistant
from test_case import ClrsTestCase
from util import range_of


class TestChapter5(ClrsTestCase):

    @given(st.data())
    def test_hire_assistant(self, data):
        n = data.draw(st.integers(min_value=1, max_value=10))
        INTERVIEWING_PREFIX = 'interviewing candidate '
        HIRING_PREFIX = 'hiring candidate '

        with patch('sys.stdout', new=StringIO()) as fake_out:
            hire_assistant(n)

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
