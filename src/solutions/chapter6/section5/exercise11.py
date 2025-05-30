from __future__ import annotations

from typing_extensions import TypeAlias

from book.data_structures import Array
from book.data_structures import PriorityQueue
from book.data_structures import Record
from solutions.chapter6.section5.exercise3 import min_heap_extract_min
from solutions.chapter6.section5.exercise3 import min_heap_insert
from util import range_of


# TODO(#20) replace by the general list node and list classes once they will have been added
class SortedListNode:
    key: float
    next: SortedListNode | None = None


class SortedList:
    head: SortedListNode | None = None


NodePayloadType: TypeAlias = tuple[SortedListNode, SortedList]


def merge_sorted_lists(sorted_lists: Array[SortedList], k: int) -> SortedList:
    """Merges sorted lists into one sorted list.

    Args:
        sorted_lists: an array of sorted lists
        k: the number of sorted lists in the array

    Returns:
        The sorted list containing all elements from the input sorted lists.
    """
    Q = PriorityQueue[NodePayloadType](k)
    for i in range_of(1, to=k):
        sorted_list = sorted_lists[i]
        if sorted_list.head is not None:
            x = sorted_list.head
            sorted_list.head = sorted_list.head.next
            x.next = None
            min_heap_insert(Q, Record[NodePayloadType](key=x.key, data=(x, sorted_list)), k)
    merged_list = SortedList()
    tail: SortedListNode | None = None
    while Q.heap_size > 0:
        head_object = min_heap_extract_min(Q)
        element, list_ = head_object.data
        if merged_list.head is None:
            tail = merged_list.head = element
        else:
            assert tail is not None
            tail.next = element
            tail = tail.next
        if list_.head is not None:
            min_heap_insert(Q, Record[NodePayloadType](key=list_.head.key, data=(list_.head, list_)), k)
            list_.head = list_.head.next
    return merged_list
