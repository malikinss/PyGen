'''
TODO:
    Implement a NumberList class that inherits from UserList and describes
    a list whose elements can only be numbers.

    When creating an instance, the class must accept one argument:
        iterable — an iterable object that defines the initial set of elements
                   of the NumberList class instance.
                   If at least one element of the passed iterable object
                   is not a number, a TypeError exception with the text must
                   be raised:
                    The elements of the NumberList class instance must be
                    numbers

    The iterable object may not be passed, in which case the initial set of
    elements is considered empty

    When modifying an instance of the NumberList class using indexes, addition
    operations (+, +=) and the append(), extend() and insert() methods,
    a check must be made that the elements being added are numbers, otherwise
    a TypeError exception with the text must be raised:
        The elements of the NumberList class instance must be numbers

NOTE:
    Instances of the int and float classes will be considered numbers.

    Instances of the NumberList class must support addition operations (+, +=)
    and the extend() method both among themselves and between any iterable
    objects.

    An instance of the NumberList class must not depend on the iterable object
    on which it was created.

    In other words, if the original iterable object changes, then the instance
    of the NumberList class must not change.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the NumberList
    class, it can be arbitrary.
'''
from collections import UserList
from collections.abc import Iterable
from typing import Union, Any


class NumberList(UserList):
    """
    Class representing a list containing only numbers (int or float).

    Inherits from UserList, ensuring all elements are numbers and validating
    additions.
    """

    _ERR_MSG = "The elements of the NumberList class instance must be numbers"

    @staticmethod
    def _is_number(obj: Any) -> bool:
        """
        Check if obj is a number (int or float).

        Args:
            obj: The object to check.

        Returns:
            bool: True if obj is int or float, False otherwise.
        """
        return isinstance(obj, (int, float))

    @staticmethod
    def _validate(obj: Any) -> None:
        """
        Validate that obj is a number or an iterable of numbers.

        Args:
            obj: The object to validate (number or iterable of numbers).

        Raises:
            TypeError: If obj is not a number or contains non-numbers.
        """
        if NumberList._is_number(obj):
            return
        if isinstance(obj, Iterable):
            if all(NumberList._is_number(x) for x in obj):
                return
        raise TypeError(NumberList._ERR_MSG)

    @staticmethod
    def _validate_item(item: Any) -> None:
        """
        Validate that item is a single number.

        Args:
            item: The item to validate (must be int or float).

        Raises:
            TypeError: If item is not a number.
        """
        if not NumberList._is_number(item):
            raise TypeError(NumberList._ERR_MSG)

    def __init__(self, iterable: Iterable[Union[int, float]] = ()) -> None:
        """
        Initialize a NumberList with elements from iterable.

        Args:
            iterable: An iterable of numbers (int or float).
                      Defaults to empty tuple.

        Raises:
            TypeError: If any element in iterable is not a number.
        """
        self._validate(iterable)
        super().__init__(iterable)

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Set item(s) at key, ensuring value(s) are numbers.

        Args:
            key: Index or slice to set.
            value: Number or iterable of numbers to assign.

        Raises:
            TypeError: If value or any element in value is not a number.
        """
        self._validate(value)
        self.data[key] = value

    def __add__(self, other: Iterable[Union[int, float]]) -> 'NumberList':
        """
        Concatenate with another iterable, returning a new NumberList.

        Args:
            other: An iterable of numbers.

        Returns:
            NumberList: A new NumberList with concatenated elements.

        Raises:
            TypeError: If any element in other is not a number.
        """
        self._validate(other)
        return NumberList(self.data + list(other))

    def __radd__(self, other: Iterable[Union[int, float]]) -> 'NumberList':
        """
        Concatenate with another iterable (left), returning a new NumberList.

        Args:
            other: An iterable of numbers.

        Returns:
            NumberList: A new NumberList with concatenated elements.

        Raises:
            TypeError: If any element in other is not a number.
        """
        self._validate(other)
        return NumberList(list(other) + self.data)

    def __iadd__(self, other: Iterable[Union[int, float]]) -> 'NumberList':
        """
        Extend the list in-place with another iterable.

        Args:
            other: An iterable of numbers.

        Returns:
            NumberList: The modified NumberList.

        Raises:
            TypeError: If any element in other is not a number.
        """
        self._validate(other)
        self.data.extend(other)
        return self

    def append(self, item: Union[int, float]) -> None:
        """Append a number to the list.

        Args:
            item: The number to append.

        Raises:
            TypeError: If item is not a number.
        """
        self._validate_item(item)
        self.data.append(item)

    def extend(self, iterable: Iterable[Union[int, float]]) -> None:
        """Extend the list with an iterable of numbers.

        Args:
            iterable: An iterable of numbers.

        Raises:
            TypeError: If any element in iterable is not a number.
        """
        self._validate(iterable)
        self.data.extend(iterable)

    def insert(self, index: int, item: Union[int, float]) -> None:
        """Insert a number at the specified index.

        Args:
            index: The index to insert at.
            item: The number to insert.

        Raises:
            TypeError: If item is not a number.
        """
        self._validate_item(item)
        self.data.insert(index, item)
