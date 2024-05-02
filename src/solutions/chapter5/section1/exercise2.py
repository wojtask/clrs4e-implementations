from random import randint


def random(a: int, b: int) -> int:
    """Returns a random integer between a and b, inclusive.

    Args:
        a: the lower endpoint of the generation range
        b: the upper endpoint of the generation range

    Returns:
        A number from the range [a, b], where each number is equally likely.
    """
    while a < b:
        mid = (a + b) // 2
        # the Random(0, 1) call is implemented as a call to the standard pseudo-random generator
        if randint(0, 1) == 0:
            a = mid + 1
        else:
            b = mid
    return a
