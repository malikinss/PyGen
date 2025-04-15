'''
TODO:
    Implement a MutableString class that describes a mutable string.

    When instantiating the class, it must accept one argument:
        string — a string that specifies the initial value of the mutable
                 string.
                 If not passed, the string is considered empty

    The MutableString class must have two instance methods:
        lower() — a method that converts all characters of the mutable string
                  to lowercase
        upper() — a method that converts all characters of the mutable string
                  to uppercase

    An instance of the MutableString class must have an informal string
    representation of the following form:
        <current value of the mutable string>

    Also, an instance of the MutableString class must have a formal string
    representation of the following form:
        MutableString('<current value of the mutable string>')

    When passing an instance of the MutableString class to the len() function,
    the number of characters in it must be returned.

    In addition, an instance of the MutableString class must be an iterable
    object, that is, it must allow iterating over its characters, for example,
    using a for loop.

    Also, an instance of the MutableString class must allow getting, changing
    and deleting the values of its elements using indexes, both positive and
    negative.

    An instance of the MutableString class must support full-fledged slices.

    The result of indexing and slices must be new mutable strings.

    Finally, instances of the MutableString class must support the addition
    operation between themselves using the + operator, the result of which
    must be a new instance of the MutableString class, representing
    the concatenation of the original ones.

NOTE:
    The implementation of the MutableString class can be arbitrary, that is,
    there are no requirements for the presence of certain attributes.

    Additional data validation in methods is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from typing import Union, Iterator


class MutableString:
    """
    A mutable string that supports character-level operations and
    concatenation.
    """

    def __init__(self, string: str = "") -> None:
        """
        Initialize with an optional string.

        Args:
            string: Initial string value (default is empty string).
        """
        self._string = list(string)

    def lower(self) -> None:
        """
        Convert all characters to lowercase in place.
        """
        self._string = list(self.__str__().lower())

    def upper(self) -> None:
        """
        Convert all characters to uppercase in place.
        """
        self._string = list(self.__str__().upper())

    def __str__(self) -> str:
        """
        Return the current string value.

        Returns:
            str: The current string.
        """
        return ''.join(self._string)

    def __repr__(self) -> str:
        """
        Return the formal string representation.

        Returns:
            str: Formal representation as MutableString('<current string>').
        """
        return f"MutableString('{self.__str__()}')"

    def __len__(self) -> int:
        """
        Return the number of characters.

        Returns:
            int: The number of characters in the string.
        """
        return len(self._string)

    def __iter__(self) -> Iterator[str]:
        """
        Yield characters of the string.

        Yields:
            str: Each character in the string.
        """
        yield from self._string

    def __getitem__(self, key: Union[int, slice]) -> 'MutableString':
        """
        Get a character or slice as a new MutableString.

        Args:
            key: Integer index or slice.

        Returns:
            MutableString: New MutableString with the selected character(s).
        """
        if isinstance(key, int):
            return MutableString(self._string[key])
        return MutableString(''.join(self._string[key]))

    def __setitem__(self, key: Union[int, slice], value: str) -> None:
        """
        Set a character or slice in place.

        Args:
            key: Integer index or slice.
            value: String to set at the index or slice.
        """
        if isinstance(key, int):
            self._string[key] = value
            self._string = list(self.__str__())
        else:
            self._string[key] = list(value)

    def __delitem__(self, key: Union[int, slice]) -> None:
        """
        Delete a character or slice in place.

        Args:
            key: Integer index or slice.
        """
        del self._string[key]

    def __add__(self, other: 'MutableString') -> 'MutableString':
        """
        Concatenate with another MutableString.

        Args:
            other: Another MutableString to concatenate.

        Returns:
            MutableString: New MutableString with concatenated value.

        Raises:
            TypeError: If other is not a MutableString.
        """
        if not isinstance(other, MutableString):
            return NotImplemented
        return MutableString(self.__str__() + other.__str__())
