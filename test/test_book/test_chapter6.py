import random

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from hypothesis.strategies import text

from book.chapter6.problem1 import build_max_heap_
from book.chapter6.section3 import build_max_heap
from book.chapter6.section4 import heapsort
from book.chapter6.section5 import max_heap_extract_max
from book.chapter6.section5 import max_heap_increase_key
from book.chapter6.section5 import max_heap_insert
from book.chapter6.section5 import max_heap_maximum
from book.data_structures import Record
from test_case import ClrsTestCase
from test_util import create_heap
from test_util import create_priority_queue


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
        records = [Record[str](key, data.draw(text())) for key in keys]
        heap = create_heap(records)
        n = len(records)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)

        actual_maximum = max_heap_maximum(A)

        expected_maximum = max(records)
        self.assertEqual(actual_maximum.key, expected_maximum.key)
        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, records, end=n)

    @given(st.data())
    def test_max_heap_maximum_underflow(self, data):
        n = data.draw(integers(min_value=1, max_value=10))
        heap = create_heap([], n)
        A = create_priority_queue(heap, n)

        with self.assertRaisesRegex(ValueError, "heap underflow"):
            max_heap_maximum(A)

    @given(st.data())
    def test_max_heap_extract_max(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        records = [Record[str](key, data.draw(text())) for key in keys]
        heap = create_heap(records)
        n = len(records)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)

        actual_maximum = max_heap_extract_max(A)

        expected_maximum = max(records)
        records.remove(actual_maximum)
        self.assertEqual(actual_maximum.key, expected_maximum.key)
        self.assertEqual(A.heap_size, n - 1)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, records, end=n - 1)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_increase_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        records = [Record[str](key, data.draw(text())) for key in keys]
        heap = create_heap(records)
        n = len(records)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)
        x = random.choice(records)
        k = x.key + data.draw(integers(min_value=0))

        max_heap_increase_key(A, x, k)

        self.assertEqual(x.key, k)
        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, records, end=n)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_increase_key_invalid_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        records = [Record[str](key, data.draw(text())) for key in keys]
        heap = create_heap(records)
        n = len(records)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)
        x = random.choice(records)
        k = x.key - data.draw(integers(min_value=1))

        with self.assertRaisesRegex(ValueError, "new key is smaller than current key"):
            max_heap_increase_key(A, x, k)

            self.assertNotEquals(x.key, k)
            self.assertMaxHeap(A)
            self.assertEqual(A.heap_size, n)
            self.assertArrayPermuted(A, records, end=n)
            self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_insert(self, data):
        n = data.draw(integers(min_value=1, max_value=100))
        keys = data.draw(lists(integers(), max_size=n - 1))
        records = [Record[str](key, data.draw(text())) for key in keys]
        heap = create_heap(records, n)
        heap_size = len(records)
        build_max_heap(heap, heap_size)
        A = create_priority_queue(heap, n)
        new_key = data.draw(integers())
        x = Record[str](new_key, data.draw(text()))

        max_heap_insert(A, x, n)

        self.assertMaxHeap(A)
        self.assertEqual(A.heap_size, heap_size + 1)
        self.assertArrayPermuted(A, records + [x], end=A.heap_size)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_insert_overflow(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        records = [Record[str](key, data.draw(text())) for key in keys]
        n = len(records)
        heap = create_heap(records)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)
        new_key = data.draw(integers())
        x = Record[str](new_key, data.draw(text()))

        with self.assertRaisesRegex(ValueError, "heap overflow"):
            max_heap_insert(A, x, n)

            self.assertMaxHeap(A)
            self.assertEqual(A.heap_size, n)
            self.assertArrayPermuted(A, records, end=n)
            self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_build_max_heap_(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        records = [Record[str](key, data.draw(text())) for key in keys]
        n = len(records)
        A = create_heap(records)

        build_max_heap_(A, n)

        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, records, end=n)
