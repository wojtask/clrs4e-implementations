def range_of(_from, to=None, downto=None, by=1):
    if downto is None:
        return range(_from, to + 1, by)
    if to is None and by is None:
        return range(_from, downto - 1, -1)
    AssertionError('Invalid range bounds')
