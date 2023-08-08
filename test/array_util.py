from book.data_structures import Array


def create_array(elements, start=1):
    n = len(elements)
    array = Array(start, n + start - 1)
    i = start
    for e in elements:
        array[i] = e
        i += 1
    return array
