def parent(i: int) -> int:
    """The index of the parent of a heap node.

    Implements:
        Parent

    Args:
        i: the index of the node

    Returns:
        The index of the parent of the node at index i.
    """
    return i // 2


def left(i: int) -> int:
    """The index of the left child of a heap node.

    Implements:
        Left

    Args:
        i: the index of the node

    Returns:
        The index of the left child of the node at index i.
    """
    return 2 * i


def right(i: int) -> int:
    """The index of the right child of a heap node.

    Implements:
        Right

    Args:
        i: the index of the node

    Returns:
        The index of the right child of the node at index i.
    """
    return 2 * i + 1
