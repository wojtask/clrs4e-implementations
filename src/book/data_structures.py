from builtins import len
from typing import Any


class Array:
    def __init__(self, start: int, end: int) -> None:
        assert 0 <= start <= end
        self.__start = start
        self.__elements = [None] * (end - start + 1)

    def __getitem__(self, index: int) -> Any:
        assert self.__start <= index < self.__start + len(self.__elements)
        return self.__elements[index - self.__start]

    def __setitem__(self, index: int, value: Any) -> None:
        assert self.__start <= index < self.__start + len(self.__elements)
        self.__elements[index - self.__start] = value


class Matrix:
    def __init__(self, rows: int, cols: int) -> None:
        assert rows >= 0 and cols >= 0
        self.__elements = [[0] * cols for _ in range(rows)]

    def __getitem__(self, indices: tuple) -> int | float:
        row = indices[0]
        col = indices[1]
        assert 1 <= row <= len(self.__elements)
        assert 1 <= col <= len(self.__elements[0])
        return self.__elements[row - 1][col - 1]

    def __setitem__(self, indices: tuple, value: int | float) -> None:
        row = indices[0]
        col = indices[1]
        assert 1 <= row <= len(self.__elements)
        assert 1 <= col <= len(self.__elements[0])
        self.__elements[row - 1][col - 1] = value

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
