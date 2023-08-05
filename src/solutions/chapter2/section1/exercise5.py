from book.data_structures import Array
from util import range_of


def add_binary_integers(A: Array, B: Array, n: int) -> Array:
    """Adds two integers, a and b, given as binary representations.

    Implements:
        Add-Binary-Integers

    Args:
        A: the 0-origin indexed Array containing the binary representation of a
        B: the 0-origin indexed Array containing the binary representation of b
        n: the length of binary representations of a and b

    Returns:
        The 0-origin indexed (n+1)-element Array containing the binary representation of a + b.
    """
    C = Array(0, n)
    carry = 0
    for i in range_of(0, to=n - 1):
        C[i] = (A[i] + B[i] + carry) % 2
        carry = (A[i] + B[i] + carry) // 2
    C[n] = carry
    return C
