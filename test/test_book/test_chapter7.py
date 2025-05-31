from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from book.chapter7.section1 import quicksort
from book.chapter7.section3 import randomized_quicksort
from book.chapter7.section4 import insertion_quicksort
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

    @given(st.data())
    def test_randomized_quicksort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        randomized_quicksort(A, 1, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_insertion_quicksort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)
        k = data.draw(integers(min_value=1, max_value=n))

        insertion_quicksort(A, 1, n, k)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)
