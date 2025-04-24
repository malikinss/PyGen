'''
TODO:
    Implement a SuperInt class that inherits from the int class and describes
    an integer with additional functionality.

    The process of creating an instance of the SuperInt class must coincide
    with the process of creating an instance of the int class.

    The SuperInt class must have four instance methods:
        repeat() - a method that takes an integer n as an argument, which is 2
                   by default, and returns an instance of the SuperInt class,
                   duplicated n times
        to_bin() - a method that returns a binary representation of
                   an instance of the SuperInt class.
                   The binary representation can be either an instance of
                   the str class or an int
        next() - a method that returns a new instance of the SuperInt class
                 that is one more than the current one
        prev() - a method that returns a new instance of the SuperInt class
                 that is one less than the current one

    Also, an instance of the SuperInt class must be an iterable object whose
    elements are its digits from left to right.

    The digits themselves must also be represented as instances of
    the SuperInt class.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the SuperInt class, it can be arbitrary.
'''
from typing import Iterator


class SuperInt(int):
    """
    Class representing an integer with additional functionality.

    Inherits from int, providing methods for repetition, binary representation,
    increment, decrement, and iteration over digits as SuperInt instances.
    """

    def repeat(self, n: int = 2) -> 'SuperInt':
        """
        Return a SuperInt instance with the number repeated n times.

        Args:
            n: Number of repetitions, defaults to 2.

        Returns:
            SuperInt: The number repeated n times (e.g., 12 repeated 2 times
                      is 1212).
        """
        str_value = str(abs(self))
        repeated = str_value * n
        return SuperInt(self._sign() * int(repeated or '0'))

    def to_bin(self) -> str:
        """
        Return the binary representation of the number.

        Returns:
            str: The binary representation without the '0b' prefix
                 (e.g., '101' for 5).
        """
        return bin(self)[2:] if self >= 0 else '-' + bin(self)[3:]

    def next(self) -> 'SuperInt':
        """
        Return a new SuperInt instance incremented by 1.

        Returns:
            SuperInt: The number plus 1.
        """
        return SuperInt(self + 1)

    def prev(self) -> 'SuperInt':
        """
        Return a new SuperInt instance decremented by 1.

        Returns:
            SuperInt: The number minus 1.
        """
        return SuperInt(self - 1)

    def __iter__(self) -> Iterator['SuperInt']:
        """
        Return an iterator over the digits of the number from left to right.

        Returns:
            Iterator[SuperInt]: An iterator yielding each digit as a SuperInt
                                instance.
        """
        str_value = str(abs(self))
        return iter(SuperInt(int(d)) for d in str_value)

    def _sign(self) -> int:
        """
        Return the sign of the number (1, -1, or 0).

        Returns:
            int: 1 for positive, -1 for negative, 0 for zero.
        """
        return 0 if self == 0 else self // abs(self)
