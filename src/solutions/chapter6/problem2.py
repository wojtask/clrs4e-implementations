from util import ceil_div


def multiary_parent(d: int, i: int) -> int:
    """The index of the parent of a multiary heap node.

    Implements:
        Multiary-Parent

    Args:
        d: the arity of the heap, d >= 2
        i: the index of the node

    Returns:
        The index of the parent of the node at index i in a d-ary heap.
    """
    return ceil_div(i - 1, d)


def multiary_child(d: int, i: int, k: int) -> int:
    """The index of a child of a multiary heap node.

    Implements:
        Multiary-Child

    Args:
        d: the arity of the heap, d >= 2
        i: the index of the node
        k: the number of a child to get, 1 <= k <= d

    Returns:
        The index of the k-th child of the node at index i in a d-ary heap.
    """
    return d * (i - 1) + k + 1
