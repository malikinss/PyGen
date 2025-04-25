'''
TODO:
    Implement a 'ValueDict' class, a 'dict' class inheritor, describing
    a dictionary with additional functionality.

    The process of creating an instance of the 'ValueDict' class must coincide
    with the process of creating an instance of the 'dict' class.

    The 'ValueDict' class must have two instance methods:
    key_of() - a method that takes a 'value' object as an argument and returns
               the first key of the 'ValueDict' class instance that has
               the 'value' value.
               If there is no such key, the method must return None.
    keys_of() - a method that takes a value object as an argument and returns
                an iterable whose elements are all the keys of the 'ValueDict'
                class instance that have the 'value' value

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the 'ValueDict'
    class, it can be arbitrary.
'''
from collections.abc import Iterable
from typing import Any


class ValueDict(dict):
    """
    Dictionary with methods to find keys by value.

    Inherits from dict, providing key retrieval by value.
    """

    def key_of(self, value: Any) -> Any | None:
        """
        Return first key for the given value or None.

        Args:
            value: Value to search.

        Returns:
            First key with the value or None if not found.
        """
        return next(self.keys_of(value), None)

    def keys_of(self, value: Any) -> Iterable[Any]:
        """
        Return iterable of keys for the given value.

        Args:
            value: Value to search.

        Returns:
            Iterable of keys with the value.
        """
        return (k for k, v in self.items() if v == value)
