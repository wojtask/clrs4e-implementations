from builtins import len
from collections.abc import MutableSequence


class Array(MutableSequence):
    def __init__(self, elements=None, first=1, last=None):
        super().__init__()
        if last is not None and elements is not None:
            raise TypeError('Cannot specify both elements and the last index')
        if last is None:
            if elements is None:
                raise TypeError('Either elements or the last index must be specified')
        else:
            elements = [None] * (last - first + 1)
        self.elements = list(elements)
        self.length = len(self.elements)
        self.first = first

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < self.first or index > self.length:
                raise IndexError('Invalid index used for addressing Array')
            return self.elements[index - self.first]
        if isinstance(index, slice):
            start = index.start if index.start is not None else self.first
            stop = index.stop if index.stop is not None else self.length
            return Array((self[i] for i in range(start, stop + 1)), first=self.first)
        if isinstance(index, tuple):
            return self[index[0]][index[1]]
        raise TypeError('Invalid type of index used for indexing Array')

    def __setitem__(self, index, value):
        if isinstance(index, int):
            if index < self.first or index > self.length:
                raise IndexError('Invalid index used for updating an Array\'s cell')
            self.elements[index - self.first] = value
        elif isinstance(index, slice):
            it = iter(value)
            start = index.start if index.start is not None else self.first
            stop = index.stop if index.stop is not None else self.length
            if len(value) != stop - start + 1:
                raise IndexError('The iterable used for updating an Array\'s fragment has different size')
            for i in range(start, stop + 1):
                self[i] = next(it)
        elif isinstance(index, tuple):
            self[index[0]][index[1]] = value
        else:
            raise TypeError('Invalid type of index used for indexing Array')
        self._modified = True

    def __delitem__(self, index):
        del self.elements[index - self.first]
        self.length -= 1
        self._modified = True

    def __len__(self):
        return self.length

    def __iter__(self):
        return iter(self.elements[:self.length])

    def __reversed__(self):
        return reversed(list(iter(self)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.first == other.first and list(iter(self)) == list(iter(other))
        return NotImplemented

    def __add__(self, other):
        return Array(list(iter(self)) + list(iter(other)), first=self.first)

    def __repr__(self):
        return '%s (first=%d, length=%d)' % (list(iter(self)), self.first, self.length)

    def insert(self, index, value):
        self.elements.insert(index - self.first, value)
        self.length += 1

    def append(self, value):
        self.insert(self.length + 1, value)
