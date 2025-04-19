'''
TODO:
    Implement a Versioned class that describes a descriptor that provides
    access to both the current value of an attribute and all previous values
    if the attribute's value has ever changed.

    The class must not take any arguments when instantiated.

    The descriptor must be assigned to an attribute that has the same name
    as the variable to which the descriptor is assigned.

    When accessing an attribute, the descriptor must return the value of that
    attribute if it is set.

    If the attribute's value is not set, an AttributeError exception must be
    raised with the text:
        Attribute not found

    When setting or changing the value of an attribute, the descriptor must
    set or change this value without any additional checks.

    The Versioned class must have two instance methods:
        - get_version() — a method that takes two arguments: an instance of
                          the class in which the descriptor is defined,
                          and an integer n.
                          The method must return the n-th value of
                          the attribute of this class instance.
                          For example, if the attribute value was set and then
                          changed, then the get_version() method must be able
                          to return both the set value (the first one) and
                          the changed value (the second one)
        - set_version() — a method that takes two arguments: an instance of
                          the class in which the descriptor is defined and
                          an integer n.
                          The method must set the n-th attribute value as
                          the current

NOTE:
    Calling the set_version() method should not be considered as changing
    the attribute value.

    We will assume that the attribute changes its value only if this operation
    is performed using dot notation or the setattr() function.

    In this case, after calling the method, the history of the attribute
    values must continue from the moment of its last change.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Versioned
    class, it can be arbitrary.
'''
from typing import Any, Optional, Type


class Versioned:
    """
    A descriptor that tracks and provides access to all previous values of
    an attribute.

    The descriptor allows setting and getting the current attribute value,
    maintaining a history of all values set via dot notation or setattr().

    It provides methods to retrieve or restore previous values using 1-based
    indexing.

    Raises:
        AttributeError: If the attribute is not set when accessed.
    """

    def __init__(self) -> None:
        """
        Initialize the descriptor with empty attribute and history key.
        """
        self._attr: str = ""
        self._history_key: str = ""

    def __set_name__(self, owner: Type[Any], attr: str) -> None:
        """
        Set the attribute name and history key for the descriptor.

        Args:
            owner: The class to which the descriptor is attached.
            attr: The name of the attribute.
        """
        self._attr = attr
        self._history_key = f"{attr}_history"

    def __get__(self, obj: Optional[object], owner: Type[Any]) -> Any:
        """
        Get the current attribute value.

        Args:
            obj: The instance of the class, or None if accessed via the class.
            owner: The class to which the descriptor is attached.

        Returns:
            The current value of the attribute.

        Raises:
            AttributeError: If the attribute is not set.
        """
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError("Attribute not found")
        return obj.__dict__[self._attr]

    def __set__(self, obj: object, value: Any) -> None:
        """
        Set or change the attribute value, adding it to the history.

        Args:
            obj: The instance of the class.
            value: The value to set.
        """
        if not self._is_history_exists(obj):
            obj.__dict__[self._history_key] = []
        obj.__dict__[self._history_key].append(value)
        obj.__dict__[self._attr] = value

    def get_version(self, obj: object, n: int) -> Any:
        """
        Get the n-th value of the attribute from its history (1-based index).

        Args:
            obj: The instance of the class.
            n: The 1-based index of the value in the history (n=1 for first
               value).

        Returns:
            The n-th value of the attribute.
        """
        return obj.__dict__[self._history_key][n - 1]

    def set_version(self, obj: object, n: int) -> None:
        """
        Set the n-th value from the history as the current attribute value
        (1-based index).

        Args:
            obj: The instance of the class.
            n: The 1-based index of the value in the history (n=1 for first
               value).
        """
        obj.__dict__[self._attr] = obj.__dict__[self._history_key][n - 1]

    def _is_history_exists(self, obj: object) -> bool:
        """
        Check if the history for the attribute exists in the instance.

        Args:
            obj: The instance of the class.

        Returns:
            bool: True if the history exists, False otherwise.
        """
        return self._history_key in obj.__dict__
