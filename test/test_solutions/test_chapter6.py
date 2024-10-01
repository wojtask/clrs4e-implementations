from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from book.chapter6.section1 import build_max_heap
from book.data_structures import Array
from solutions.chapter6.section2.exercise3 import min_heapify
from test_case import ClrsTestCase
from test_util import create_array
from util import range_of


def build_min_heap_by_inversion(A: Array, n: int) -> None:
    """Relies on the fact that when we replace each element of a max heap by the element's opposite, the resulting array
    is a min heap."""
    build_max_heap(A, n)
    for i in range_of(1, to=n):
        A[i] = -A[i]


class TestChapter6(ClrsTestCase):

    @given(st.data())
    def test_min_heapify(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        n = len(elements)
        A = create_array([-x for x in elements])
        build_min_heap_by_inversion(A, n)
        self.assertMinHeap(A)
        new_root = data.draw(integers(max_value=A[1] - 1))
        elements.remove(A[1])
        elements.append(new_root)
        A[1] = new_root  # possibly violate the min-heap property at the root

        min_heapify(A, 1)

        self.assertEqual(A.heap_size, n)
        self.assertMinHeap(A)
        self.assertArrayPermuted(A, elements, end=n)
