from __future__ import annotations

from typing import Generic

from book.data_structures import Array
from book.data_structures import KeyObject
from book.data_structures import PriorityQueue
from book.data_structures import T
from solutions.chapter6.section5.exercise3 import min_heap_extract_min
from solutions.chapter6.section5.exercise3 import min_heap_insert
from util import range_of


# TODO(#20) replace by the general list node and list classes once they will have been added
class SortedListNode(Generic[T]):
    key: T
    next: SortedListNode[T] | None = None


class SortedList(Generic[T]):
    head: SortedListNode[T] | None = None


def merge_sorted_lists(sorted_lists: Array[SortedList[T]], k: int) -> SortedList[T]:
    """Merges sorted lists into one sorted list.

    Args:
        sorted_lists: an array of sorted lists
        k: the number of sorted lists in the array

    Returns:
        The sorted list containing all elements from the input sorted lists.
    """
    Q = PriorityQueue(k)
    for i in range_of(1, to=k):
        sorted_list = sorted_lists[i]
        if sorted_list.head is not None:
            x = sorted_list.head
            sorted_list.head = sorted_list.head.next
            x.next = None
            min_heap_insert(Q, KeyObject(key=x.key, data=(x, sorted_list)), k)
    merged_list = SortedList[T]()
    tail = None
    while Q.heap_size > 0:
        element, list_ = min_heap_extract_min(Q).data
        if merged_list.head is None:
            tail = merged_list.head = element
        else:
            tail.next = element
            tail = tail.next
        if list_.head is not None:
            min_heap_insert(Q, KeyObject(key=list_.head.key, data=(list_.head, list_)), k)
            list_.head = list_.head.next
    return merged_list
