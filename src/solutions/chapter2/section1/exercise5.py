from book.data_structures import Array
from book.data_structures import Bit
from util import range_of


def add_binary_integers(A: Array[Bit], B: Array[Bit], n: int) -> Array[Bit]:
    """Adds two integers, a and b, given as binary representations.

    Implements:
        Add-Binary-Integers

    Args:
        A: the 0-origin indexed Array containing the binary representation of a
        B: the 0-origin indexed Array containing the binary representation of b
        n: the length of binary representations of a and b

    Returns:
        The 0-origin indexed (n+1)-element Array containing the binary representation of a + b.
    """
    C = Array[Bit](0, n)
    carry = 0
    for i in range_of(0, to=n - 1):
        C[i] = (A[i] + B[i] + carry) % 2  # type: ignore
        carry = (A[i] + B[i] + carry) // 2
    C[n] = carry  # type: ignore
    return C

def main():
    # Your main logic goes here
    # print(add_binary_integers(Array()))
    array_bit_ = Array[Bit](0, 2)
    array_bit_[0] = 1
    array_bit_[1] = 0
    array_bit_[2] = 1
    print("first array: " + array_bit_.__str__())

    array_bit_1 = Array[Bit](0, 2)
    array_bit_1[0] = 0
    array_bit_1[1] = 0
    array_bit_1[2] = 1
    print("second array: " + array_bit_1.__str__())
    print("resulting array: " + add_binary_integers(array_bit_, array_bit_1, 2).__str__())

if __name__ == "__main__":
    main()
