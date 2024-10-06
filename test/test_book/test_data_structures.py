from hypothesis import assume
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers

from book.data_structures import Array
from test_case import ClrsTestCase
from util import range_of


class TestArray(ClrsTestCase):

    @given(st.data())
    def test_set_get_elements(self, data):
        n = data.draw(integers(min_value=1, max_value=10))
        index = data.draw(integers(min_value=1, max_value=n))
        element = data.draw(integers())
        array = Array[int](1, n)

        array[index] = element

        self.assertEqual(array[index], element)

    @given(st.data())
    def test_new_array_is_empty(self, data):
        n = data.draw(integers(min_value=1, max_value=10))
        array = Array[int](1, n)

        for i in range_of(1, to=n):
            self.assertIsNone(array[i])

    @given(st.data())
    def test_create_array_with_negative_start(self, data):
        start = data.draw(integers(max_value=-1))

        with self.assertRaises(AssertionError):
            Array[int](start, 10)

    @given(st.data())
    def test_create_array_with_invalid_index_range(self, data):
        start = data.draw(integers(min_value=0, max_value=10))
        end = data.draw(integers(min_value=0, max_value=10))
        assume(start > end)

        with self.assertRaises(AssertionError):
            Array[int](start, end)

    @given(st.data())
    def test_access_by_invalid_index(self, data):
        n = data.draw(integers(min_value=1, max_value=10))
        index = data.draw(integers(min_value=1, max_value=10))
        assume(index > n)
        array = Array[int](1, n)

        with self.assertRaises(AssertionError):
            _ = array[index]

    @given(st.data())
    def test_mutate_by_invalid_index(self, data):
        n = data.draw(integers(min_value=1, max_value=10))
        index = data.draw(integers(min_value=1, max_value=10))
        element = data.draw(integers())
        assume(index > n)
        array = Array[int](1, n)

        with self.assertRaises(AssertionError):
            array[index] = element
