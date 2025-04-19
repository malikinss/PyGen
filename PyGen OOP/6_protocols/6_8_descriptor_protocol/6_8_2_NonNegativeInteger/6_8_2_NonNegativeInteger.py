'''
TODO:
    Implement the NonNegativeInteger class, which describes a descriptor
    that checks that the attribute value being set or changed is
    a non-negative integer.

    When instantiated, the class must accept two arguments in the following
    order:
        name — the name of the attribute to which the descriptor will
               be attached
        default — the default value. If not passed, it is None

    When accessing an attribute, the descriptor must return the value of that
    attribute, if it is set.

    If the value is not set, the default value specified when the descriptor
    was created must be returned.

    If the default value is None, an AttributeError exception must be raised
    with the text:
        Attribute not found

    When setting or changing the value of an attribute, the descriptor must
    check that the value is a non-negative integer.

    If the value is not a non-negative integer, a ValueError exception should
    be raised with the text:
        Invalid value

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with valid data.

    There are no restrictions regarding the implementation of
    the NonNegativeInteger class, it can be arbitrary.
'''
from typing import Any, Optional, Type


class NonNegativeInteger:
    """
    A descriptor that ensures an attribute value is a non-negative integer.

    Args:
        name: The name of the attribute to which the descriptor is attached.
        default: The default value to return if the attribute is not set.
                 Defaults to None.

    Raises:
        AttributeError: If the attribute is not set and no default value
                        is provided.
        ValueError: If the attribute value is not a non-negative integer.
    """

    def __init__(self, name: str, default: Optional[int] = None) -> None:
        """
        Initialize the descriptor with the attribute name and default value.

        Args:
            name: The name of the attribute.
            default: The default value, if any. Defaults to None.
        """
        self._attr: str = name
        self._default: Optional[int] = default

    def __get__(self, obj: Optional[object], owner: Type[Any]) -> Any:
        """
        Get the attribute value or default value.

        Args:
            obj: The instance of the class, or None if accessed via the class.
            owner: The class to which the descriptor is attached.

        Returns:
            The value of the attribute or the default value.

        Raises:
            AttributeError: If the attribute is not set and default is None.
        """
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        if self._default is not None:
            return self._default
        raise AttributeError("Attribute not found")

    def __set__(self, obj: object, value: Any) -> None:
        """
        Set the attribute value, ensuring it is a non-negative integer.

        Args:
            obj: The instance of the class.
            value: The value to set.

        Raises:
            ValueError: If the value is not a non-negative integer.
        """
        if not self.__is_non_negative_int(value):
            raise ValueError("Invalid value")
        obj.__dict__[self._attr] = value

    @staticmethod
    def __is_non_negative_int(value: Any) -> bool:
        """
        Check if the value is a non-negative integer.

        Args:
            value: The value to check.

        Returns:
            bool: True if the value is an integer and non-negative,
                  False otherwise.
        """
        return isinstance(value, int) and value >= 0
