from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from book.chapter6.section1 import build_max_heap
from test_case import ClrsTestCase
from test_util import create_array


class TestChapter6(ClrsTestCase):

    @given(st.data())
    def test_build_max_heap(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        build_max_heap(A, n)

        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, elements, end=n)
