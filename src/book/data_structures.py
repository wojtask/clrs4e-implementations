from builtins import len


class Array:
    def __init__(self, start, end):
        assert 0 <= start <= end, 'Invalid indexes range'
        super().__init__()
        self.__start = start
        self.__elements = [None] * (end - start + 1)

    def __getitem__(self, index):
        assert self.__start <= index < self.__start + len(
            self.__elements), 'Invalid index used for accessing an Array cell'
        return self.__elements[index - self.__start]

    def __setitem__(self, index, value):
        assert self.__start <= index < self.__start + len(
            self.__elements), 'Invalid index used for mutating an Array cell'
        self.__elements[index - self.__start] = value

    def __repr__(self):
        return '[%d:%d]: %s' % self.__start, len(self.__elements), (list(iter(self.__elements)))
