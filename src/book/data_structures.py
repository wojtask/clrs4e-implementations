from __future__ import annotations

from builtins import len
from collections.abc import Callable
from typing import Any
from typing import Generic
from typing import Literal
from typing import TypeVar

from typing_extensions import Protocol

T = TypeVar('T')
CT = TypeVar('CT', bound='Comparable')


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool:
        pass

    def __le__(self, other: Any) -> bool:
        pass

    def __gt__(self, other: Any) -> bool:
        pass

    def __ge__(self, other: Any) -> bool:
        pass


class Indexable(Protocol[T]):
    __getitem__: Callable[[int], T]
    __setitem__: Callable[[int, T], None]


Bit = Literal[0, 1]


class Array(Generic[T]):
    __start: int
    __elements: list[T]

    def __init__(self, start: int, end: int) -> None:
        assert 0 <= start <= end
        self.__start = start
        self.__elements = [None] * (end - start + 1)  # type: ignore

    def __getitem__(self, index: int) -> T:
        assert self.__start <= index < self.__start + len(self.__elements)
        return self.__elements[index - self.__start]

    def __setitem__(self, index: int, value: T) -> None:
        assert self.__start <= index < self.__start + len(self.__elements)
        self.__elements[index - self.__start] = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        for i, element in enumerate(self.__elements, start=self.__start):
            if element != other[i]:
                return False
        return True

    def __repr__(self) -> str:
        return '%d-based: %s' % (self.__start, self.__elements)


class Matrix:
    __start_row: int
    __end_row: int
    __start_col: int
    __end_col: int
    __elements: list[list[int]]

    def __init__(self, end_row: int, end_col: int, start_row: int = 1, start_col: int = 1,
                 elements: list[list[int]] | None = None) -> None:
        if elements is None:
            assert start_row == 1
            assert start_col == 1
            self.__elements = [[0] * end_col for _ in range(end_row)]
        else:
            self.__elements = elements
        self.__start_row, self.__end_row = start_row, end_row
        self.__start_col, self.__end_col = start_col, end_col

    def submatrix(self, rows: tuple[int, int], cols: tuple[int, int]) -> "Matrix":
        assert 1 <= rows[0] <= rows[1] <= len(self.__elements)
        assert 1 <= cols[0] <= cols[1] <= len(self.__elements[0])
        rows_shifted = rows[0] + self.__start_row - 1, rows[1] + self.__start_row - 1
        cols_shifted = cols[0] + self.__start_col - 1, cols[1] + self.__start_col - 1
        return Matrix(start_row=rows_shifted[0], end_row=rows_shifted[1], start_col=cols_shifted[0],
                      end_col=cols_shifted[1], elements=self.__elements)

    def even_rows_submatrix(self) -> "Matrix":
        even_rows = [row for i, row in enumerate(self.__elements, start=1) if i % 2 == 0]
        submatrix_end_row = self.__start_row + len(even_rows) - 1
        return Matrix(start_row=self.__start_row, end_row=submatrix_end_row, start_col=self.__start_col,
                      end_col=self.__end_col, elements=even_rows)

    def __getitem__(self, indices: tuple[int, int]) -> int:
        row, col = indices[0], indices[1]
        assert 1 <= row <= self.__end_row - self.__start_row + 1
        assert 1 <= col <= self.__end_col - self.__start_col + 1
        return self.__elements[self.__start_row - 1 + row - 1][self.__start_col - 1 + col - 1]

    def __setitem__(self, indices: tuple[int, int], value: int) -> None:
        row, col = indices[0], indices[1]
        assert 1 <= row <= self.__end_row - self.__start_row + 1
        assert 1 <= col <= self.__end_col - self.__start_col + 1
        self.__elements[self.__start_row - 1 + row - 1][self.__start_col - 1 + col - 1] = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        for i, row in enumerate(self.__elements, start=1):
            for j, element in enumerate(row, start=1):
                if element != other[i, j]:
                    return False
            try:
                _ = other[i, len(row) + 1]
                return False
            except AssertionError:
                pass
        try:
            _ = other[len(self.__elements) + 1, 1]
            return False
        except AssertionError:
            pass
        return True

    def __repr__(self) -> str:
        return repr(
            [row[self.__start_col - 1: self.__end_col] for row in
             self.__elements[self.__start_row - 1: self.__end_row]])
