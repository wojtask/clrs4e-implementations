import random
from typing import Union

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from hypothesis.strategies import text

from book.chapter6.section3 import build_max_heap
from book.data_structures import CT
from book.data_structures import Heap
from book.data_structures import KeyObject
from book.data_structures import PriorityQueue
from solutions.chapter6.problem2 import multiary_child
from solutions.chapter6.problem2 import multiary_parent
from solutions.chapter6.section2.exercise3 import min_heapify
from solutions.chapter6.section2.exercise6 import iterative_max_heapify
from solutions.chapter6.section5.exercise10 import max_heap_delete
from solutions.chapter6.section5.exercise3 import min_heap_decrease_key
from solutions.chapter6.section5.exercise3 import min_heap_extract_min
from solutions.chapter6.section5.exercise3 import min_heap_insert
from solutions.chapter6.section5.exercise3 import min_heap_minimum
from solutions.chapter6.section5.exercise4 import max_heap_decrease_key
from solutions.chapter6.section5.exercise8 import max_heap_increase_key_
from test_case import ClrsTestCase
from test_util import create_heap
from util import range_of


def build_min_heap_by_inversion(A: Union[Heap[CT], Heap[KeyObject]], n: int) -> None:
    """Relies on the fact that when we replace each element of a max-heap by the element's opposite, the resulting array
    is a min-heap."""
    build_max_heap(A, n)
    for i in range_of(1, to=n):
        if isinstance(A[i], KeyObject):
            A[i].key = -A[i].key
        else:
            A[i] = -A[i]


class TestChapter6(ClrsTestCase):

    @given(st.data())
    def test_min_heapify(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        n = len(elements)
        A = create_heap([-x for x in elements])
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

    @given(st.data())
    def test_iterative_max_heapify(self, data):
        elements = data.draw(lists(integers(), min_size=1))
        n = len(elements)
        A = create_heap(elements)
        build_max_heap(A, n)
        new_root = data.draw(integers(max_value=A[1] - 1))
        elements.remove(A[1])
        elements.append(new_root)
        A[1] = new_root  # possibly violate the max-heap property at the root

        iterative_max_heapify(A, 1)

        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, elements, end=n)

    @given(st.data())
    def test_min_heap_minimum(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = PriorityQueue(heap, n)

        actual_minimum = min_heap_minimum(A)

        expected_minimum = min(key_objects)
        self.assertEqual(actual_minimum.key, expected_minimum.key)
        self.assertEqual(A.heap_size, n)
        self.assertMinHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n)

    @given(st.data())
    def test_min_heap_minimum_underflow(self, data):
        n = data.draw(integers(min_value=1, max_value=10))
        heap = create_heap([], n)
        A = PriorityQueue(heap, n)

        with self.assertRaisesRegex(ValueError, "heap underflow"):
            min_heap_minimum(A)

    @given(st.data())
    def test_min_heap_extract_min(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = PriorityQueue(heap, n)

        actual_minimum = min_heap_extract_min(A)

        expected_minimum = min(key_objects)
        key_objects.remove(actual_minimum)
        self.assertEqual(actual_minimum.key, expected_minimum.key)
        self.assertEqual(A.heap_size, n - 1)
        self.assertMinHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n - 1)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_min_heap_decrease_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = PriorityQueue(heap, n)
        x = random.choice(key_objects)
        k = x.key - data.draw(integers(min_value=0))

        min_heap_decrease_key(A, x, k)

        self.assertEqual(x.key, k)
        self.assertEqual(A.heap_size, n)
        self.assertMinHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_min_heap_decrease_key_invalid_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = PriorityQueue(heap, n)
        x = random.choice(key_objects)
        k = x.key + data.draw(integers(min_value=1))

        with self.assertRaisesRegex(ValueError, "new key is larger than current key"):
            min_heap_decrease_key(A, x, k)

            self.assertNotEquals(x.key, k)
            self.assertMinHeap(A)
            self.assertEqual(A.heap_size, n)
            self.assertArrayPermuted(A, key_objects, end=n)
            self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_min_heap_insert(self, data):
        n = data.draw(integers(min_value=1, max_value=100))
        keys = data.draw(lists(integers(), max_size=n - 1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects, n)
        heap_size = len(key_objects)
        build_min_heap_by_inversion(heap, heap_size)
        A = PriorityQueue(heap, n)
        new_key = data.draw(integers())
        x = KeyObject(new_key, data.draw(text()))

        min_heap_insert(A, x, n)

        self.assertMinHeap(A)
        self.assertEqual(A.heap_size, heap_size + 1)
        self.assertArrayPermuted(A, key_objects + [x], end=A.heap_size)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_min_heap_insert_overflow(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        n = len(key_objects)
        heap = create_heap(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = PriorityQueue(heap, n)
        new_key = data.draw(integers())
        x = KeyObject(new_key, data.draw(text()))

        with self.assertRaisesRegex(ValueError, "heap overflow"):
            min_heap_insert(A, x, n)

            self.assertMinHeap(A)
            self.assertEqual(A.heap_size, n)
            self.assertArrayPermuted(A, key_objects, end=n)
            self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_decrease_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = PriorityQueue(heap, n)
        x = random.choice(key_objects)
        k = x.key - data.draw(integers(min_value=0))

        max_heap_decrease_key(A, x, k)

        self.assertEqual(x.key, k)
        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_decrease_key_invalid_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = PriorityQueue(heap, n)
        x = random.choice(key_objects)
        k = x.key + data.draw(integers(min_value=1))

        with self.assertRaisesRegex(ValueError, "new key is larger than current key"):
            max_heap_decrease_key(A, x, k)

            self.assertNotEquals(x.key, k)
            self.assertMaxHeap(A)
            self.assertEqual(A.heap_size, n)
            self.assertArrayPermuted(A, key_objects, end=n)
            self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_increase_key_(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, '') for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = PriorityQueue(heap, n)
        x = random.choice(key_objects)
        k = x.key + data.draw(integers(min_value=0))

        max_heap_increase_key_(A, x, k)

        self.assertEqual(x.key, k)
        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_delete(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, '') for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = PriorityQueue(heap, n)
        x = random.choice(key_objects)

        max_heap_delete(A, x)

        key_objects.remove(x)
        self.assertEqual(A.heap_size, n - 1)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n - 1)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_increase_key__invalid_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject(key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = PriorityQueue(heap, n)
        x = random.choice(key_objects)
        k = x.key - data.draw(integers(min_value=1))

        with self.assertRaisesRegex(ValueError, "new key is smaller than current key"):
            max_heap_increase_key_(A, x, k)

            self.assertNotEquals(x.key, k)
            self.assertMaxHeap(A)
            self.assertEqual(A.heap_size, n)
            self.assertArrayPermuted(A, key_objects, end=n)
            self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_multiary_parent_child(self, data):
        d = data.draw(integers(min_value=2, max_value=20))
        i = data.draw(integers(min_value=1))
        k = data.draw(integers(min_value=1, max_value=d))

        actual_node_index = multiary_parent(d, multiary_child(d, i, k))

        self.assertEqual(actual_node_index, i)
