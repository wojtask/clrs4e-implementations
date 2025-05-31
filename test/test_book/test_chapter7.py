import math

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from book.chapter7.problem1 import hoare_partition
from book.chapter7.problem4 import stooge_sort
from book.chapter7.problem5 import tre_quicksort
from book.chapter7.section1 import quicksort
from book.chapter7.section3 import randomized_quicksort
from book.chapter7.section4 import insertion_quicksort
from book.chapter7.section4 import median_of_3_partition
from test_case import ClrsTestCase
from test_util import create_array
from util import range_of


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

    @given(st.data())
    def test_median_of_3_partition(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        actual_pivot_index = median_of_3_partition(A, 1, n)

        for i in range_of(1, to=actual_pivot_index):
            self.assertLessEqual(A[i], A[actual_pivot_index])
        for i in range_of(actual_pivot_index + 1, to=n):
            self.assertGreaterEqual(A[i], A[actual_pivot_index])
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_hoare_partition(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        actual_split_index = hoare_partition(A, 1, n)

        left_max = -math.inf
        right_min = math.inf
        for i in range_of(1, to=actual_split_index):
            left_max = max(left_max, A[i])
        for i in range_of(actual_split_index + 1, to=n):
            right_min = min(right_min, A[i])
        self.assertLessEqual(left_max, right_min)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_stooge_sort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        stooge_sort(A, 1, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_tre_quicksort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_array(elements)
        n = len(elements)

        tre_quicksort(A, 1, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)
