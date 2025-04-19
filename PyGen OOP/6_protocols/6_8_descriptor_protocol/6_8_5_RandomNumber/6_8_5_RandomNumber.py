'''
TODO:
    Implement a RandomNumber class that describes a handle that, when accessed,
    returns a random integer in a given range.

    When instantiated, the class must accept three arguments in the following
    order:
        start — integer
        end — integer
        cache — Boolean, defaults to False

    The handle must be assigned to an attribute that has the same name
    as the variable to which the handle is assigned.

    When accessed, the handle must return a random integer between start and
    end inclusive.

    If the cache parameter was set to True when the handle was created, each
    time the attribute is accessed, the handle must return the number that was
    generated the first time.

    When setting or changing the value of the attribute, the handle must raise
    an AttributeError exception with the text:
        Change is not possible

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the RandomNumber
    class, it can be arbitrary.
'''
import random
from typing import Any, Optional, Type


class RandomNumber:
    """
    A descriptor that returns a random integer in a given range when accessed.

    Args:
        start: The lower bound of the random integer range (inclusive).
        end: The upper bound of the random integer range (inclusive).
        cache: If True, returns the first generated number on subsequent
               accesses.
               Defaults to False.

    Raises:
        AttributeError: If an attempt is made to set or change the attribute
                        value.
    """

    def __init__(self, start: int, end: int, cache: bool = False) -> None:
        """
        Initialize the descriptor with range and caching settings.

        Args:
            start: The lower bound of the random integer range.
            end: The upper bound of the random integer range.
            cache: Whether to cache the first generated number.
                   Defaults to False.
        """
        self._start: int = start
        self._end: int = end
        self._cache: bool = cache
        self._generated: Optional[int] = None
        self._attr: str = ""

    def __set_name__(self, owner: Type[Any], attr: str) -> None:
        """
        Set the attribute name for the descriptor.

        Args:
            owner: The class to which the descriptor is attached.
            attr: The name of the attribute.
        """
        self._attr = attr

    def __get__(self, obj: Optional[object], owner: Type[Any]) -> int:
        """
        Get a random integer in the specified range.

        Args:
            obj: The instance of the class, or None if accessed via the class.
            owner: The class to which the descriptor is attached.

        Returns:
            A random integer in the range [start, end].
        """
        if obj is None:
            return self
        if self._cache and self._generated is not None:
            return self._generated
        self._generated = random.randint(self._start, self._end)
        return self._generated

    def __set__(self, obj: object, value: Any) -> None:
        """
        Prevent setting or changing the attribute value.

        Args:
            obj: The instance of the class.
            value: The value attempted to be set.

        Raises:
            AttributeError: Always raised with message:
                                'Change is not possible'
        """
        raise AttributeError("Change is not possible")
