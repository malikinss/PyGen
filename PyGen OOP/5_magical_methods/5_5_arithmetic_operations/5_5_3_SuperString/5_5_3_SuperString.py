'''
TODO:
    Implement a SuperString class that describes a string.

    When instantiated, the class must accept one argument:
        string — the string value

    An instance of the SuperString class must have the following informal
    string representation:
        <string value>

    In addition, instances of the SuperString class must support addition
    between themselves using the + operator, the result of which must be a new
    instance of the SuperString class representing the concatenation of
    the original ones.

    An instance of the SuperString class must also support multiplication,
    division, bitwise left shift, and bitwise right shift by an integer n
    using the *, /, <<, and >> operators, respectively:
        - the result of multiplication must be a new instance of
          the SuperString class representing the original string multiplied
          by n.
        - the result of division shall be a new instance of the SuperString
          class representing the string consisting of the first m characters
          of the original string, where m is the length of the original string
          divided by n
        - the result of a bitwise left shift shall be a new instance of
          the SuperString class representing the original string without
          the last n characters.
          If n is greater than or equal to the length of the original string,
          the result shall be an instance of the SuperString class
          representing the empty string
        - the result of a bitwise right shift shall be a new instance of
          the SuperString class representing the original string without
          the first n characters.
          If n is greater than or equal to the length of the original string,
          the result shall be an instance of the SuperString class
          representing the empty string

    The multiplication operation shall be performable regardless of the order
    of the operands, i.e. it shall be possible to multiply both a string by
    a number and a number by a string.

NOTE:
    It is guaranteed that an instance of the SuperString class is always
    divisible by a non-zero number.

    If the object with which the arithmetic operation is performed is invalid,
    the method implementing this operation must return the NotImplemented
    constant.

    There are no restrictions regarding the implementation of the SuperString
    class, it can be arbitrary.
'''
from typing import Union


class SuperString:
    """
    A class representing a string with extended operations.
    """

    def __init__(self, string: str) -> None:
        """
        Initialize SuperString with a string value.

        Args:
            string (str): The string value.
        """
        self.string = string

    def __str__(self) -> str:
        """
        Informal string representation of the SuperString.

        Returns:
            str: The string value.
        """
        return self.string

    def __add__(
        self, other: 'SuperString'
    ) -> 'Union[SuperString, NotImplemented]':  # type: ignore
        """
        Concatenate two SuperString instances.

        Args:
            other (SuperString): Another SuperString instance to concatenate.

        Returns:
            SuperString: New instance with concatenated strings.
            NotImplemented: If other is not a SuperString instance.
        """
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(
        self, n: int
    ) -> 'Union[SuperString, NotImplemented]':  # type: ignore
        """
        Multiply SuperString by an integer.

        Args:
            n (int): Number of times to repeat the string.

        Returns:
            SuperString: New instance with the string repeated n times.
            NotImplemented: If n is not an integer.
        """
        if isinstance(n, int):
            return SuperString(self.string * n)
        return NotImplemented

    def __rmul__(
        self, n: int
    ) -> 'Union[SuperString, NotImplemented]':  # type: ignore
        """
        Right multiply SuperString by an integer (n * SuperString).

        Args:
            n (int): Number of times to repeat the string.

        Returns:
            SuperString: New instance with the string repeated n times.
            NotImplemented: If n is not an integer.
        """
        return self.__mul__(n)

    def __truediv__(
        self, n: int
    ) -> 'Union[SuperString, NotImplemented]':  # type: ignore
        """
        Divide SuperString by an integer.

        Args:
            n (int): Divisor to determine the length of the resulting string.

        Returns:
            SuperString: New instance with the first m characters,
                         where m is len(string) // n.
            NotImplemented: If n is not an integer.
        """
        if isinstance(n, int):
            m = len(self.string) // n
            return SuperString(self.string[:m])
        return NotImplemented

    def __lshift__(
        self, n: int
    ) -> 'Union[SuperString, NotImplemented]':  # type: ignore
        """
        Bitwise left shift: remove last n characters.

        Args:
            n (int): Number of characters to remove from the end.

        Returns:
            SuperString: New instance without the last n characters,
                         or empty if n >= length.
            NotImplemented: If n is not an integer.
        """
        if isinstance(n, int):
            if n == 0:
                return SuperString(self.string)
            if n >= len(self.string):
                return SuperString("")
            return SuperString(self.string[:-n])
        return NotImplemented

    def __rshift__(
        self, n: int
    ) -> 'Union[SuperString, NotImplemented]':  # type: ignore
        """
        Bitwise right shift: remove first n characters.

        Args:
            n (int): Number of characters to remove from the start.

        Returns:
            SuperString: New instance without the first n characters,
                         or empty if n >= length.
            NotImplemented: If n is not an integer.
        """
        if isinstance(n, int):
            if n == 0:
                return SuperString(self.string)
            if n >= len(self.string):
                return SuperString("")
            return SuperString(self.string[n:])
        return NotImplemented
