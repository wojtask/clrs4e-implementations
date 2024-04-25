def range_of(_from, to=None, downto=None, by=None):
    if downto is None:
        return range(_from, to + 1, 1 if by is None else by)
    if to is None and by is None:
        return range(_from, downto - 1, -1)
    AssertionError('Invalid range bounds')


def ceil_div(x, y):
    return -(x // -y)
