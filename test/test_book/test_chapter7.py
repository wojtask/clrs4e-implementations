from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from book.chapter7.section1 import quicksort
from test_case import ClrsTestCase
from test_util import create_array


class TestChapter7(ClrsTestCase):

    @given(st.data())
    def test_quicksort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        quicksort(A, 1, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)
