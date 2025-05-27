from __future__ import annotations

import math
import random

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import floats
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from hypothesis.strategies import text

from book.chapter6.section3 import build_max_heap
from book.data_structures import Array
from book.data_structures import CT
from book.data_structures import Heap
from book.data_structures import KeyObject
from book.data_structures import T
from solutions.chapter6.problem2 import multiary_child
from solutions.chapter6.problem2 import multiary_parent
from solutions.chapter6.problem3 import young_extract_min
from solutions.chapter6.problem3 import young_insert
from solutions.chapter6.problem3 import young_sort
from solutions.chapter6.section2.exercise3 import min_heapify
from solutions.chapter6.section2.exercise6 import iterative_max_heapify
from solutions.chapter6.section5.exercise10 import max_heap_delete
from solutions.chapter6.section5.exercise11 import SortedList
from solutions.chapter6.section5.exercise11 import SortedListNode
from solutions.chapter6.section5.exercise11 import merge_sorted_lists
from solutions.chapter6.section5.exercise3 import min_heap_decrease_key
from solutions.chapter6.section5.exercise3 import min_heap_extract_min
from solutions.chapter6.section5.exercise3 import min_heap_insert
from solutions.chapter6.section5.exercise3 import min_heap_minimum
from solutions.chapter6.section5.exercise4 import max_heap_decrease_key
from solutions.chapter6.section5.exercise8 import max_heap_increase_key_
from solutions.chapter6.section5.exercise9 import ControlledPriorityQueue
from solutions.chapter6.section5.exercise9 import max_heap_pop
from solutions.chapter6.section5.exercise9 import max_heap_push
from solutions.chapter6.section5.exercise9 import min_heap_dequeue
from solutions.chapter6.section5.exercise9 import min_heap_enqueue
from test_case import ClrsTestCase
from test_util import create_array
from test_util import create_heap
from test_util import create_matrix
from test_util import create_priority_queue
from util import range_of


def build_min_heap_by_inversion(A: Heap[CT] | Heap[KeyObject[T]], n: int) -> None:
    """Relies on the fact that when we replace each element of a max-heap by the element's opposite, the resulting array
    is a min-heap."""
    build_max_heap(A, n)
    for i in range_of(1, to=n):
        if isinstance(A[i], KeyObject):
            A[i].key = -A[i].key
        else:
            A[i] = -A[i]


def create_sorted_list(elements: list[T]) -> SortedList:
    sortedList = SortedList()
    tail: SortedListNode | None = None
    for element in elements:
        x = SortedListNode()
        x.key = element
        if sortedList.head is None:
            sortedList.head = x
            tail = x
        else:
            assert tail is not None
            tail.next = x
            tail = x
    return sortedList


def convert_sorted_list(sorted_list: SortedList) -> list[T]:
    result = []
    x = sorted_list.head
    while x is not None:
        result.append(x.key)
        x = x.next
    return result


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
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = create_priority_queue(heap, n)

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
        A = create_priority_queue(heap, n)

        with self.assertRaisesRegex(ValueError, "heap underflow"):
            min_heap_minimum(A)

    @given(st.data())
    def test_min_heap_extract_min(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = create_priority_queue(heap, n)

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
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = create_priority_queue(heap, n)
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
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = create_priority_queue(heap, n)
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
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects, n)
        heap_size = len(key_objects)
        build_min_heap_by_inversion(heap, heap_size)
        A = create_priority_queue(heap, n)
        new_key = data.draw(integers())
        x = KeyObject[str](new_key, data.draw(text()))

        min_heap_insert(A, x, n)

        self.assertMinHeap(A)
        self.assertEqual(A.heap_size, heap_size + 1)
        self.assertArrayPermuted(A, key_objects + [x], end=A.heap_size)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_min_heap_insert_overflow(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        n = len(key_objects)
        heap = create_heap(key_objects)
        build_min_heap_by_inversion(heap, n)
        A = create_priority_queue(heap, n)
        new_key = data.draw(integers())
        x = KeyObject[str](new_key, data.draw(text()))

        with self.assertRaisesRegex(ValueError, "heap overflow"):
            min_heap_insert(A, x, n)

            self.assertMinHeap(A)
            self.assertEqual(A.heap_size, n)
            self.assertArrayPermuted(A, key_objects, end=n)
            self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_decrease_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)
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
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)
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
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)
        x = random.choice(key_objects)
        k = x.key + data.draw(integers(min_value=0))

        max_heap_increase_key_(A, x, k)

        self.assertEqual(x.key, k)
        self.assertEqual(A.heap_size, n)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_max_heap_increase_key__invalid_key(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)
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
    def test_min_heap_queue(self, data):
        # simulate the queue - enqueue, dequeue, then again enqueue and dequeue
        keys1 = data.draw(lists(integers(), min_size=10, max_size=20))
        d1 = data.draw(integers(min_value=1, max_value=len(keys1)))
        keys2 = data.draw(lists(integers(), min_size=10, max_size=20))
        d2 = data.draw(integers(min_value=1, max_value=len(keys1) - d1 + len(keys2)))
        key_objects1 = [KeyObject[str](key, data.draw(text())) for key in keys1]
        key_objects2 = [KeyObject[str](key, data.draw(text())) for key in keys2]
        n = 100
        A = ControlledPriorityQueue[str](n)

        for x in key_objects1:
            min_heap_enqueue(A, x, n)

        self.assertMinHeap(A)
        self.assertArrayPermuted(A, key_objects1, end=len(key_objects1))
        self.assertPriorityQueueMappingConsistent(A)

        for i in range_of(1, to=d1):
            actual_key_object = min_heap_dequeue(A)
            self.assertEqual(actual_key_object, key_objects1[i - 1])

        for x in key_objects2:
            min_heap_enqueue(A, x, n)

        self.assertMinHeap(A)
        expected_key_objects = key_objects1[d1:] + key_objects2
        self.assertArrayPermuted(A, expected_key_objects, end=len(expected_key_objects))
        self.assertPriorityQueueMappingConsistent(A)

        for i in range_of(1, to=d2):
            actual_key_object = min_heap_dequeue(A)
            self.assertEqual(actual_key_object, expected_key_objects[i - 1])

    @given(st.data())
    def test_max_heap_stack(self, data):
        # simulate the stack - push, pop, then again push and pop
        keys1 = data.draw(lists(integers(), min_size=10, max_size=20))
        d1 = data.draw(integers(min_value=1, max_value=len(keys1)))
        keys2 = data.draw(lists(integers(), min_size=10, max_size=20))
        d2 = data.draw(integers(min_value=1, max_value=len(keys1) - d1 + len(keys2)))
        key_objects1 = [KeyObject[str](key, data.draw(text())) for key in keys1]
        key_objects2 = [KeyObject[str](key, data.draw(text())) for key in keys2]
        n = 100
        A = ControlledPriorityQueue[str](n)

        for x in key_objects1:
            max_heap_push(A, x, n)

        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, key_objects1, end=len(key_objects1))
        self.assertPriorityQueueMappingConsistent(A)

        for i in range_of(1, to=d1):
            actual_key_object = max_heap_pop(A)
            self.assertEqual(actual_key_object, key_objects1[-i])

        for x in key_objects2:
            max_heap_push(A, x, n)

        self.assertMaxHeap(A)
        expected_key_objects = key_objects1[:-d1] + key_objects2
        self.assertArrayPermuted(A, expected_key_objects, end=len(expected_key_objects))
        self.assertPriorityQueueMappingConsistent(A)

        for i in range_of(1, to=d2):
            actual_key_object = max_heap_pop(A)
            self.assertEqual(actual_key_object, expected_key_objects[-i])

    @given(st.data())
    def test_max_heap_delete(self, data):
        keys = data.draw(lists(integers(), min_size=1))
        key_objects = [KeyObject[str](key, data.draw(text())) for key in keys]
        heap = create_heap(key_objects)
        n = len(key_objects)
        build_max_heap(heap, n)
        A = create_priority_queue(heap, n)
        x = random.choice(key_objects)

        max_heap_delete(A, x)

        key_objects.remove(x)
        self.assertEqual(A.heap_size, n - 1)
        self.assertMaxHeap(A)
        self.assertArrayPermuted(A, key_objects, end=n - 1)
        self.assertPriorityQueueMappingConsistent(A)

    @given(st.data())
    def test_merge_sorted_lists(self, data):
        k = data.draw(integers(min_value=1, max_value=10))
        sorted_lists = [create_sorted_list(data.draw(lists(integers(), min_size=1, max_size=10).map(sorted)))
                        for _ in range_of(1, to=k)]
        sorted_lists_array = create_array(sorted_lists)
        all_elements = []
        for sorted_list in sorted_lists:
            all_elements.extend(convert_sorted_list(sorted_list))

        actual_merged_list = merge_sorted_lists(sorted_lists_array, k)

        actual_all_elements = convert_sorted_list(actual_merged_list)
        actual_all_elements_array = create_array(actual_all_elements)
        n = len(all_elements)
        self.assertArraySorted(actual_all_elements_array, end=n)
        self.assertArrayPermuted(actual_all_elements_array, all_elements, end=n)

    @given(st.data())
    def test_multiary_parent_child(self, data):
        d = data.draw(integers(min_value=2, max_value=20))
        i = data.draw(integers(min_value=1))
        k = data.draw(integers(min_value=1, max_value=d))

        actual_node_index = multiary_parent(d, multiary_child(d, i, k))

        self.assertEqual(actual_node_index, i)

    @given(st.data())
    def test_young_tableau(self, data):
        m = data.draw(integers(min_value=1, max_value=10))
        n = data.draw(integers(min_value=1, max_value=10))
        elements = data.draw(lists(floats(min_value=-1000, max_value=1000), min_size=1, max_size=m * n))
        size = len(elements)
        Y = create_matrix([[math.inf] * n for _ in range_of(1, to=m)])
        self.assertYoungTableau(Y, m, n)

        for element in elements:
            young_insert(Y, m, n, element)
            self.assertYoungTableau(Y, m, n)

        actual_elements = Array(1, size)
        for i in range_of(1, to=size):
            actual_elements[i] = young_extract_min(Y, m, n)
            self.assertYoungTableau(Y, m, n)

        self.assertArraySorted(actual_elements, end=size)

    @given(st.data())
    def test_young_sort(self, data):
        n = data.draw(integers(min_value=1, max_value=10))
        elements = data.draw(lists(integers(), min_size=n * n, max_size=n * n))
        A = create_array(elements)

        young_sort(A, n)

        self.assertArraySorted(A, end=n * n)
        self.assertArrayPermuted(A, elements, end=n * n)
