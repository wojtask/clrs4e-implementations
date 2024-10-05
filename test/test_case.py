import operator
import unittest
from collections.abc import Callable
from typing import Any

from book.chapter6.section1 import left
from book.chapter6.section1 import right
from book.data_structures import Array
from util import range_of


class ClrsTestCase(unittest.TestCase):

    def assertArraySorted(self, array: Array, start: int = 1, end: int = None,
                          cmp: Callable[[Any, Any], bool] = operator.le) -> None:
        if start >= end:
            return
        for i in range_of(start, to=end - 1):
            if not cmp(array[i], array[i + 1]):
                self.fail(f'Array {array} is not sorted according to the relation {cmp}: '
                          f'elements ${array[i]}, ${array[i + 1]} are out of order')

    def assertArrayPermuted(self, array: Array, elements: list, start: int = 1, end: int = None) -> None:
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

    def assertHeap(self, heap, cmp: Callable[[Any, Any], bool]) -> None:
        msg = f'Array {heap} is not a max-heap'

        def assertMaxSubheap(i: int) -> None:
            l = left(i)
            if l <= heap.heap_size:
                if not cmp(heap[i], heap[l]):
                    self.fail(msg)
                assertMaxSubheap(l)
            r = right(i)
            if r <= heap.heap_size:
                if not cmp(heap[i], heap[r]):
                    self.fail(msg)
                assertMaxSubheap(r)

        assertMaxSubheap(1)

    def assertMaxHeap(self, heap) -> None:
        self.assertHeap(heap, lambda x, y: x >= y)

    def assertMinHeap(self, heap) -> None:
        self.assertHeap(heap, lambda x, y: x <= y)
