'''
TODO:
    Implement a BitArray class that describes a bit list, that is, a list
    whose elements are only zeros and ones.

    When instantiating the class, it must accept one argument:
        iterable — an iterable defining the initial set of elements of the bit
                   list.
                   If not passed, the initial set is considered empty

    An instance of the BitArray class must have the following informal string
    representation:
        [
            <first element of the bit list>,
            <second element of the bit list>, ...
        ]

    Passing an instance of the BitArray class to the len() function must
    return the number of elements in it.

    Passing an instance of the BitArray class to the reversed() function must
    return an iterator whose elements are the elements of the passed instance
    of the BitArray class, arranged in reverse order.

    An instance of the BitArray class must be an iterable object, that is,
    it must allow its elements to be iterated over, for example, using
    a for loop.

    In addition, an instance of the BitArray class must support the membership
    operation using the in operator.

    Also, an instance of the BitArray class must allow the values of its
    elements to be retrieved using indices, both positive and negative.

    In addition, an instance of the BitArray class must support the unary
    operator ~, which performs the logical negation operation on each bit of
    the bit list, thereby converting 0 to 1, and 1 to 0.

    The result of the operator
    must be a new instance of the BitArray class.

    Finally, instances of the BitArray class must support logical operations
    between themselves using the & and | operators:
        the & operator must perform the logical AND operation on each pair
        of bits of two bit lists of equal length.

        The result of the operator must be a new instance of the BitArray class

        the | operator must perform the logical OR operation on each pair
        of bits of two bit lists of equal length.

        The result of the operator must be a new instance of the BitArray class

NOTE:
    Before deciding, think about which abstract class from the collections.abc
    module would be convenient as a parent.

    An instance of the BitArray class must not depend on the iterable object
    on which it was created.

    In other words, if the original iterable object changes, the instance of
    the BitArray class must not change.

    If the object with which a logical operation is performed is invalid,
    the method implementing this operation must return the NotImplemented
    constant.

    There are no restrictions regarding the implementation of the BitArray
    class, it can be arbitrary.
'''
from collections.abc import Sequence, Iterable
from typing import Any, Union, Iterator


class BitArray(Sequence):
    """
    Sequence of bits (0 or 1) with logical operations.

    Supports iteration, indexing, length, membership, reversal, and bitwise
    operations.
    """

    def __init__(self, iterable: Iterable[int] = ()) -> None:
        """
        Initialize with an iterable of bits (0 or 1).

        Args:
            iterable: Iterable of 0s and 1s. Defaults to empty.
        """
        self.arr = list(iterable)

    def __str__(self) -> str:
        """
        Return string representation of the bit array.

        Returns:
            str: String in the format '[<bit1>, <bit2>, ...]'.
        """
        return str(self.arr)

    def __len__(self) -> int:
        """
        Return the number of bits.

        Returns:
            int: Length of the bit array.
        """
        return len(self.arr)

    def __getitem__(self, key: Union[int, slice]) -> Any:
        """
        Get bit or slice by index.

        Args:
            key: Integer index or slice.

        Returns:
            Bit or subsequence.
        """
        return self.arr[key]

    def __contains__(self, value: Any) -> bool:
        """
        Check if value is in the bit array.

        Args:
            value: Value to check (0 or 1).

        Returns:
            bool: True if value is in the array, False otherwise.
        """
        return value in self.arr

    def __reversed__(self) -> Iterator[int]:
        """
        Return iterator of bits in reverse order.

        Returns:
            Iterator[int]: Reverse iterator over the bit array.
        """
        return iter(self.arr[::-1])

    def __invert__(self) -> 'BitArray':
        """
        Return new BitArray with inverted bits (0 -> 1, 1 -> 0).

        Returns:
            BitArray: New BitArray with inverted bits.
        """
        return BitArray(1 - bit for bit in self.arr)

    def __and__(self, other: Any) -> 'BitArray':
        """
        Return new BitArray with bitwise AND of two BitArrays.

        Args:
            other: Another BitArray of the same length.

        Returns:
            BitArray: New BitArray with bitwise AND result.
            NotImplemented: If other is not a BitArray or has different length.
        """
        if not isinstance(other, BitArray) or len(self) != len(other):
            return NotImplemented
        return BitArray(a & b for a, b in zip(self.arr, other.arr))

    def __or__(self, other: Any) -> 'BitArray':
        """
        Return new BitArray with bitwise OR of two BitArrays.

        Args:
            other: Another BitArray of the same length.

        Returns:
            BitArray: New BitArray with bitwise OR result.
            NotImplemented: If other is not a BitArray or has different length.
        """
        if not isinstance(other, BitArray) or len(self) != len(other):
            return NotImplemented
        return BitArray(a | b for a, b in zip(self.arr, other.arr))
