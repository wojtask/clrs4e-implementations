from builtins import len
from typing import Any
from typing import Tuple
from typing import Union


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
    def __init__(self, rows: Union[int, Tuple[int, int]], cols: Union[int, Tuple[int, int]], elements=None) -> None:
        if isinstance(rows, int) and isinstance(cols, int) and elements is None:
            assert rows >= 0
            assert cols >= 0
            self.__create_matrix(rows, cols)
        elif isinstance(rows, tuple) and isinstance(cols, tuple) and elements is not None:
            self.__create_submatrix(rows, cols, elements)
        else:
            raise TypeError('Invalid parameters')

    def __create_matrix(self, rows, cols):
        self.__start_row, self.__end_row = 1, rows
        self.__start_col, self.__end_col = 1, cols
        self.__elements = [[0] * cols for _ in range(rows)]

    def __create_submatrix(self, rows, cols, elements):
        self.__start_row, self.__end_row = rows[0], rows[1]
        self.__start_col, self.__end_col = cols[0], cols[1]
        self.__elements = elements

    def submatrix(self, rows: Tuple[int, int], cols: Tuple[int, int]):
        assert 1 <= rows[0] <= rows[1] <= len(self.__elements)
        assert 1 <= cols[0] <= cols[1] <= len(self.__elements[0])
        rows_shifted = rows[0] + self.__start_row - 1, rows[1] + self.__start_row - 1
        cols_shifted = cols[0] + self.__start_col - 1, cols[1] + self.__start_col - 1
        return Matrix(rows_shifted, cols_shifted, self.__elements)

    def even_rows_submatrix(self):
        even_rows = [row for i, row in enumerate(self.__elements, start=1) if i % 2 == 0]
        submatrix_rows_indices = self.__start_row, self.__start_row + len(even_rows) - 1
        return Matrix(submatrix_rows_indices, (self.__start_col, self.__end_col), even_rows)

    def __getitem__(self, indices: Tuple[int, int]) -> Union[int, float]:
        row = indices[0]
        col = indices[1]
        assert 1 <= row <= self.__end_row - self.__start_row + 1
        assert 1 <= col <= self.__end_col - self.__start_col + 1
        return self.__elements[self.__start_row - 1 + row - 1][self.__start_col - 1 + col - 1]

    def __setitem__(self, indices: Tuple[int, int], value: Union[int, float]) -> None:
        row = indices[0]
        col = indices[1]
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
