from __future__ import annotations

from collections.abc import Iterable


def range_of(_from: int,
             *,
             to: int | None = None,
             downto: int | None = None,
             by: int | None = None) -> Iterable:
    if to is not None and downto is None:
        return range(_from, to + 1, 1 if by is None else by)
    if to is None and downto is not None and by is None:
        return range(_from, downto - 1, -1)
    raise AssertionError('Invalid range bounds')


def ceil_div(x: int, y: int) -> int:
    return -(x // -y)
