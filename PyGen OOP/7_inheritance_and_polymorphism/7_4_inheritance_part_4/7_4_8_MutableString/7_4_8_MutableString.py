'''
TODO:
    Implement a `MutableString` class that inherits from the `UserString` class
    and describes a mutable string.

    The process of creating an instance of the `MutableString` class must be
    the same as the process of creating an instance of the `UserString` class.

    The `MutableString` class must have three instance methods:
        lower() — a method that converts all characters of the mutable string
                  to lowercase
        upper() — a method that converts all characters of the mutable string
                  to uppercase
        sort() — a method that sorts the characters of the mutable string.

    It can take two optional named arguments, key and reverse, that perform
    the same task as in the sorted() function

    An instance of the `MutableString` class must allow getting, changing,
    and deleting the values of its elements using indexes, both positive and
    negative.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the `MutableString` class, it can be arbitrary.
'''
from collections import UserString
from typing import Union, Iterator, Any, Callable
from typing import Optional as Opt


class MutableString(UserString):
    """
    Mutable string supporting character modifications and case/sort operations.

    Inherits from UserString, allowing indexing, slicing, and in-place changes.
    """

    def __init__(self, string: Any = "") -> None:
        """
        Initialize with a string, storing as a list of characters.

        Args:
            string: Initial string value. Defaults to empty string.
        """
        super().__init__(string)
        self.data = list(str(self.data))

    def lower(self) -> None:
        """
        Convert all characters to lowercase in-place.
        """
        self.data = list(str(self).lower())

    def upper(self) -> None:
        """
        Convert all characters to uppercase in-place.
        """
        self.data = list(str(self).upper())

    def sort(
        self, *, key: Opt[Callable[[str], Any]] = None, reverse: bool = False
    ) -> None:
        """
        Sort characters in-place, optionally with key and reverse.

        Args:
            key: Function to transform characters for sorting.
                 Defaults to None.
            reverse: Sort in descending order if True. Defaults to False.
        """
        self.data = list(sorted(self.data, key=key, reverse=reverse))

    def __str__(self) -> str:
        """
        Return string representation.
        """
        return "".join(self.data)

    def __repr__(self) -> str:
        """
        Return formal string representation.
        """
        return f"MutableString('{self}')"

    def __len__(self) -> int:
        """
        Return length of the string.
        """
        return len(self.data)

    def __iter__(self) -> Iterator[str]:
        """
        Return iterator over characters.
        """
        return iter(self.data)

    def __getitem__(self, key: Union[int, slice]) -> 'MutableString':
        """
        Get character or substring by index or slice.

        Args:
            key: Integer index or slice.

        Returns:
            MutableString: Single character or substring.
        """
        if isinstance(key, int):
            return MutableString(self.data[key])
        return MutableString("".join(self.data[key]))

    def __setitem__(self, key: Union[int, slice], value: str) -> None:
        """
        Set character or substring by index or slice.

        Args:
            key: Integer index or slice.
            value: Single character (for index) or string (for slice).
        """
        if isinstance(key, int):
            if len(value) != 1:
                raise ValueError("Value must be a single character for index")
            self.data[key] = value
        else:
            self.data[key] = list(value)

    def __delitem__(self, key: Union[int, slice]) -> None:
        """
        Delete character or substring by index or slice.

        Args:
            key: Integer index or slice.
        """
        del self.data[key]
