from typing import Iterable
from typing import Union


def range_of(_from: int, to: int = None, downto: int = None, by: int = None) -> Iterable:
    if downto is None:
        return range(_from, to + 1, 1 if by is None else by)
    if to is None and by is None:
        return range(_from, downto - 1, -1)
    AssertionError('Invalid range bounds')


def ceil_div(x: Union[int, float], y: Union[int, float]) -> int:
    return -(x // -y)
