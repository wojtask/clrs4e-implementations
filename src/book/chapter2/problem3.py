from book.data_structures import Array
from util import range_of




def horner(A: Array, n: int, x: float) -> float:
    """Evaluates a polynomial for a given value using Horner's rule.

    Implements:
        Horner

    Args:
        A: a 0-origin indexed array of the polynomial's coefficients;
            A[i] contains the coefficient of x^i
        n: the degree of the polynomial
        x: the value the polynomial is evaluated for

    Returns:
        The value of the polynomial for x.
    """
    p = 0
    for i in range_of(n, downto=0):
        p = A[i] + x * p
    return p
