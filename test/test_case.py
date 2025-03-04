import operator
import unittest
from collections.abc import Callable
from typing import Any

from book.chapter6.section1 import parent
from book.data_structures import Array
from book.data_structures import CT
from book.data_structures import Heap
from book.data_structures import PriorityQueue
from book.data_structures import T
from util import range_of


class ClrsTestCase(unittest.TestCase):

    def assertArraySorted(self, array: Array[CT], end: int, start: int = 1,
                          cmp: Callable[[Any, Any], bool] = operator.le) -> None:
        if start >= end:
            return
        for i in range_of(start, to=end - 1):
            if not cmp(array[i], array[i + 1]):
                self.fail(f'Array {array} is not sorted according to the relation {cmp}: '
                          f'elements ${array[i]}, ${array[i + 1]} are out of order')

    def assertArrayPermuted(self, array: Array[T], elements: list[T], end: int, start: int = 1) -> None:
        msg = f'Array {array} is not a permutation of {elements}'
        if end - start + 1 != len(elements):
            self.fail(msg)
        for i in range_of(start, to=end):
            if array[i] not in elements:
                self.fail(msg)
        for e in elements:
            match = False
            for i in range_of(start, to=end):
                if array[i] == e:
                    match = True
                    break
            if not match:
                self.fail(msg)

    def assertHeap(self, heap: Heap[CT], heap_property: Callable[[int], bool]) -> None:
        for i in range_of(2, to=heap.heap_size):
            self.assertTrue(heap_property(i))

    def assertMaxHeap(self, heap: Heap[CT]) -> None:
        self.assertHeap(heap, lambda i: heap[parent(i)] >= heap[i])

    def assertMinHeap(self, heap: Heap[CT]) -> None:
        self.assertHeap(heap, lambda i: heap[parent(i)] <= heap[i])

    def assertPriorityQueueMappingConsistent(self, queue: PriorityQueue) -> None:
        for i in range_of(1, to=queue.heap_size):
            self.assertEqual(queue.mapping[queue[i]], i)
