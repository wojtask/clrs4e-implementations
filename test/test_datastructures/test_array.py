from unittest import TestCase

from hamcrest import *

from datastructures.array import Array


class TestArray(TestCase):

    def setUp(self):
        self.elements = [5, 2, 4, 6, 1, 3]
        self.array = Array(self.elements)

    def test_has_correct_length(self):
        assert_that(self.array.length, is_(6))

    def test_gets_element(self):
        assert_that(self.array[3], is_(4))

    def test_sets_element(self):
        self.array[2] = 3
        assert_that(self.array.elements[1], is_(3))

    def test_elements_are_copied(self):
        new_array = Array(self.elements)
        new_array[2] = 100
        assert_that(self.array.elements[1], is_not(100))

    def test_gets_all_elements(self):
        assert_that([x for x in self.array], is_(self.elements))

    def test_gets_infix_subarray(self):
        actual_subarray = self.array[3:4]
        expected_subarray = Array([4, 6])
        assert_that(actual_subarray, is_(expected_subarray))

    def test_gets_prefix_subarray(self):
        actual_subarray = self.array[:4]
        expected_subarray = Array([5, 2, 4, 6])
        assert_that(actual_subarray, is_(expected_subarray))

    def test_gets_suffix_subarray(self):
        actual_subarray = self.array[5:]
        expected_subarray = Array([1, 3])
        assert_that(actual_subarray, is_(expected_subarray))

    def test_addressing_by_invalid_slice(self):
        try:
            self.array[3:10]
        except IndexError:
            return
        self.fail()

    def test_instantiate_with_custom_first_index(self):
        array = Array(self.elements, first=0)
        assert_that(array.first, is_(0))
        assert_that(array.length, is_(6))
        assert_that(array[3], is_(6))

    def test_create_empty_array_with_custom_indexes(self):
        array = Array(first=0, last=7)
        assert_that(array.first, is_(0))
        assert_that(array.length, is_(8))
        assert_that(array[3], is_(none()))

    def test_insert_at_specified_index(self):
        self.array.insert(3, 9)
        assert_that(self.array.elements[2], is_(9))

    def test_append_element(self):
        self.array.append(9)
        assert_that(self.array.length, is_(7))
        assert_that(self.array.elements[-1], is_(9))

    def test_extend(self):
        self.array.extend([8, 7])
        assert_that(self.array.length, is_(8))
        assert_that(self.array.elements[-2:], is_([8, 7]))
