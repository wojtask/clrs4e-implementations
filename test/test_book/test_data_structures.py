from hypothesis import given, assume
from hypothesis.strategies import integers

from book.data_structures import Array
from test_case import ClrsTestCase
from util import range_of


class TestArray(ClrsTestCase):

    @given(integers(min_value=1, max_value=10), integers(min_value=1, max_value=10), integers())
    def test_set_get_elements(self, n, index, element):
        assume(index <= n)
        array = Array(1, n)

        array[index] = element

        self.assertEqual(array[index], element)

    @given(integers(min_value=1, max_value=10))
    def test_new_array_is_empty(self, n):
        array = Array(1, n)

        for i in range_of(1, to=n):
            self.assertIsNone(array[i])

    @given(integers(max_value=-1))
    def test_create_array_with_negative_start(self, start):
        try:
            Array(start, 10)
        except AssertionError:
            return
        self.fail()

    @given(integers(min_value=0, max_value=10), integers(min_value=0, max_value=10))
    def test_create_array_with_invalid_index_range(self, start, end):
        assume(start > end)
        try:
            Array(start, end)
        except AssertionError:
            return
        self.fail()

    @given(integers(min_value=1, max_value=10), integers(min_value=2, max_value=15))
    def test_access_by_invalid_index(self, n, index):
        assume(index > n)
        array = Array(1, n)
        try:
            array[index]
        except AssertionError:
            return
        self.fail()

    @given(integers(min_value=1, max_value=10), integers(min_value=2, max_value=15), integers())
    def test_mutate_by_invalid_index(self, n, index, element):
        assume(index > n)
        array = Array(1, n)
        try:
            array[index] = element
        except AssertionError:
            return
        self.fail()
