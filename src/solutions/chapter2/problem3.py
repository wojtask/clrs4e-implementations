from book.data_structures import Array
from util import range_of


def polynomial_evaluate(A: Array, n: int, x: float) -> float:
    """Evaluates a polynomial for a given value using the naive method.

    Implements:
        Polynomial-Evaluate

    Args:
        A: a 0-origin indexed array of the polynomial's coefficients;
            A[i] contains the coefficient of x^i
        n: the degree of the polynomial
        x: the value the polynomial is evaluated for

    Returns:
        The value of the polynomial for x.
    """
    p = 0
    for i in range_of(0, to=n):
        s = A[i]
        for j in range_of(1, to=i):
            s *= x
        p += s
    return p
