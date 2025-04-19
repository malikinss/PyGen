'''
TODO:
    Implement a TypeChecked class that describes a descriptor that checks that
    the attribute value being set or changed is of a certain data type.

    When instantiated, the class must accept an arbitrary number of positional
    arguments, each of which is a data type.

    The descriptor must be attached to an attribute that has the same name
    as the variable to which the descriptor is assigned.

    When accessing an attribute, the descriptor must return the value
    of that attribute, if it is set.

    If the attribute value is not set, an AttributeError exception must be
    raised with the text:
        Attribute not found

    When setting or changing the value of an attribute, the descriptor must
    check whether the value is of one of the types specified when
    the descriptor was created.

    If the value is not of any type, a TypeError exception must be raised with
    the text:
        Invalid value

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the TypeChecked
    class, it can be arbitrary.
'''
from typing import Any, Optional, Type


class TypeChecked:
    """
    A descriptor that ensures an attribute value is of specified types.

    Args:
        *args: The data types the attribute value must match.

    Raises:
        AttributeError: If the attribute is not set.
        TypeError: If the attribute value is not of the specified types.
    """

    def __init__(self, *args: type) -> None:
        """
        Initialize the descriptor with allowed types.

        Args:
            *args: The data types the attribute value must match.
        """
        self._types: tuple[type, ...] = tuple(args)
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
        Get the attribute value.

        Args:
            obj: The instance of the class, or None if accessed via the class.
            owner: The class to which the descriptor is attached.

        Returns:
            The value of the attribute.

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
        Set the attribute value, ensuring it matches the specified types.

        Args:
            obj: The instance of the class.
            value: The value to set.

        Raises:
            TypeError: If the value is not of the specified types.
        """
        if not isinstance(value, self._types):
            raise TypeError("Invalid value")
        obj.__dict__[self._attr] = value
