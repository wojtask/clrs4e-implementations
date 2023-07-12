from unittest import TestCase

from hamcrest import *

from book.data_structures import Array


class TestArray(TestCase):

    def test_set_get_elements(self):
        array = Array(1, 3)
        array[1] = 1
        array[2] = 42
        array[3] = -16
        assert_that(array[1], is_(1))
        assert_that(array[2], is_(42))
        assert_that(array[3], is_(-16))

    def test_new_array_is_empty(self):
        array = Array(1, 3)
        assert_that(array[1], is_(None))
        assert_that(array[2], is_(None))
        assert_that(array[3], is_(None))

    def test_create_array_with_negative_index(self):
        try:
            Array(-1, 3)
        except AssertionError:
            return
        self.fail()

    def test_create_array_with_invalid_index_range(self):
        try:
            Array(4, 3)
        except AssertionError:
            return
        self.fail()

    def test_access_by_invalid_index(self):
        array = Array(1, 3)
        try:
            array[5]
        except AssertionError:
            return
        self.fail()

    def test_mutate_by_invalid_index(self):
        array = Array(1, 3)
        try:
            array[0] = 2
        except AssertionError:
            return
        self.fail()
