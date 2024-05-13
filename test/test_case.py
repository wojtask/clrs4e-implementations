import operator
import unittest
from typing import Any
from typing import Callable
from typing import List

from book.data_structures import Array
from util import range_of


class ClrsTestCase(unittest.TestCase):

    def assertArraySorted(self, array: Array, start: int = 1, end: int = None,
                          cmp: Callable[[Any, Any], bool] = operator.le) -> Any:
        if start >= end:
            return
        for i in range_of(start, to=end - 1):
            if not cmp(array[i], array[i + 1]):
                self.fail(f'Array {array} is not sorted according to the relation {cmp}: '
                          f'elements ${array[i]}, ${array[i + 1]} are out of order')

    def assertArrayPermuted(self, array: Array, elements: List, start: int = 1, end: int = None) -> Any:
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
