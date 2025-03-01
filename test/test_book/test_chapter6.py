import random

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from hypothesis.strategies import text

from book.chapter6.section3 import build_max_heap
from book.chapter6.section4 import heapsort
from book.chapter6.section5 import max_heap_extract_max
from book.chapter6.section5 import max_heap_increase_key
from book.chapter6.section5 import max_heap_insert
from book.chapter6.section5 import max_heap_maximum
from book.data_structures import KeyObject
from book.data_structures import PriorityQueue
from test_case import ClrsTestCase
from test_util import create_heap


class TestChapter6(ClrsTestCase):

    @given(st.data())
    def test_build_max_heap(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_heap(elements)
        n = len(elements)

        build_max_heap(A, n)

        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_heapsort(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        A = create_heap(elements)
        n = len(elements)

        heapsort(A, n)

        self.assertArraySorted(A, end=n)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_max_heap_maximum(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = PriorityQueue(heap, n)

        actual_maximum = max_heap_maximum(A)

        expected_maximum = max(key_objects)
        self.assertEqual(actual_maximum.key, expected_maximum.key)
        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n)

    @given(st.data())
    def test_max_heap_maximum_underflow(self, data):
        n = data.draw(integers(min_value=1, max_value=10))
        heap = create_heap([], n)
        A = PriorityQueue(heap, n)

        with self.assertRaises(ValueError, msg="heap underflow"):
            max_heap_maximum(A)

    @given(st.data())
    def test_max_heap_extract_max(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = PriorityQueue(heap, n)

        actual_maximum = max_heap_extract_max(A)

        expected_maximum = max(key_objects)
        key_objects.remove(actual_maximum)
        self.assertEqual(actual_maximum.key, expected_maximum.key)
        self.assertEqual(A.heap_size, n - 1)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n - 1)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_increase_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = PriorityQueue(heap, n)
        x = random.choice(key_objects)
        k = x.key + data.draw(integers(min_value=0))

        max_heap_increase_key(A, x, k)

        self.assertEqual(x.key, k)
        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_increase_key_invalid_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = PriorityQueue(heap, n)
        x = random.choice(key_objects)
        k = x.key - data.draw(integers(min_value=1))

        with self.assertRaises(ValueError, msg="new key is smaller than current key"):
            max_heap_increase_key(A, x, k)

            self.assertNotEquals(x.key, k)
            self.assertMaxHeap(A)
            self.assertEqual(A.heap_size, n)
            self.assertArrayPermuted(A, key_objects, end=n)
            self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_insert(self, data):
        n = data.draw(integers(min_value=1, max_value=100))
        keys = data.draw(lists(integers(), max_size=n - 1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects, n)
        heap_size = len(key_objects)
        build_max_heap(heap, heap_size)
        A = PriorityQueue(heap, n)
        new_key = data.draw(integers())
        x = KeyObject(new_key, data.draw(text()))

        max_heap_insert(A, x, n)

        self.assertMaxHeap(A)
        self.assertEqual(A.heap_size, heap_size + 1)
        self.assertArrayPermuted(A, key_objects + [x], end=A.heap_size)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_insert_overflow(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        n = len(key_objects)
        heap = create_heap(key_objects)
        A = PriorityQueue(heap, n)
        new_key = data.draw(integers())
        x = KeyObject(new_key, data.draw(text()))

        with self.assertRaises(ValueError, msg="heap overflow"):
            max_heap_insert(A, x, n)

            self.assertMaxHeap(A)
            self.assertEqual(A.heap_size, n)
            self.assertArrayPermuted(A, key_objects, end=n)
            self.assertPriorityQueueMappingConsistent(A)
