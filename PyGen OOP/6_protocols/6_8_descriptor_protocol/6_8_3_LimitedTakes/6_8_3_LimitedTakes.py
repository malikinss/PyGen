'''
TODO:
    Implement a LimitedTakes class that describes a descriptor that allows
    the attribute value to be retrieved only a certain number of times.

    When instantiated, the class must accept one argument:
        times — the number of times the attribute can be accessed

    The descriptor must be assigned to an attribute that has the same name
    as the variable to which the descriptor is assigned.

    When accessing an attribute, the descriptor must return the value
    of that attribute, if it is set.

    If the attribute value is not set, an AttributeError exception must
    be raised with the text:
        Attribute not found

    If the attribute has been accessed times, then all subsequent accesses
    must raise a MaxCallsException exception with the text:
        The number of times the attribute can be accessed has been exceeded

    When setting or changing the attribute value, the descriptor must set or
    change this value without any additional checks.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the LimitedTakes
    class, it can be arbitrary.
'''
from typing import Any, Optional, Type


class MaxCallsException(Exception):
    """
    Exception raised when the attribute access limit is exceeded.
    """
    pass


class LimitedTakes:
    """
    A descriptor that limits the number of times an attribute can be accessed.

    Args:
        times: The number of times the attribute can be accessed.

    Raises:
        AttributeError: If the attribute is not set.
        MaxCallsException: If the attribute access limit is exceeded.
    """

    def __init__(self, times: int) -> None:
        """
        Initialize the descriptor with the access limit.

        Args:
            times: The number of times the attribute can be accessed.
        """
        self._limit: int = times
        self._counter: int = 0
        self._attr: str = ""

    def __set_name__(self, owner: Type[Any], attr: str) -> None:
        """
        Set the attribute name for the descriptor.

        Args:
            owner: The class to which the descriptor is attached.
            attr: The name of the attribute.
        """
        self._attr = attr

    def __get__(self, obj: Optional[object], owner: Type[Any]) -> Any:
        """
        Get the attribute value, tracking access count.

        Args:
            obj: The instance of the class, or None if accessed via the class.
            owner: The class to which the descriptor is attached.

        Returns:
            The value of the attribute.

        Raises:
            AttributeError: If the attribute is not set.
            MaxCallsException: If the access limit is exceeded.
        """
        if obj is None:
            return self
        if self._counter >= self._limit:
            raise MaxCallsException(
                "Number of times the attr can be accessed has been exceeded"
            )
        if self._attr not in obj.__dict__:
            raise AttributeError("Attribute not found")
        self._counter += 1
        return obj.__dict__[self._attr]

    def __set__(self, obj: object, value: Any) -> None:
        """
        Set the attribute value without restrictions.

        Args:
            obj: The instance of the class.
            value: The value to set.
        """
        obj.__dict__[self._attr] = value
