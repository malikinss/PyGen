'''
TODO:
    Implement a NonKeyword class that describes a descriptor that checks that
    the attribute value being set or changed is not a Python string keyword.

    When instantiated, the class must accept one argument:
        name — the name of the attribute to which the descriptor will be
               attached

    When accessing an attribute, the descriptor must return the value of
    that attribute, if it is set.

    If the attribute value is not set, an AttributeError exception must
    be raised with the text:
        Attribute not found

    When setting or changing the attribute value, the descriptor must check
    whether the value is a Python string keyword.

    If the value is a string keyword, a ValueError exception must be raised
    with the text:
        Invalid value

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with valid data.

    There are no restrictions on the implementation of the NonKeyword class,
    it can be arbitrary.
'''
import keyword
from typing import Any, Optional, Type


class NonKeyword:
    """
    A descriptor that ensures an attribute value is not a Python keyword
    string.

    Args:
        name: The name of the attribute to which the descriptor is attached.

    Raises:
        AttributeError: If the attribute is accessed but not set.
        ValueError: If the attribute value is a Python keyword string.
    """

    def __init__(self, name: str) -> None:
        self._attr: str = name

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        """
        Set the attribute name for the descriptor.

        Args:
            owner: The class to which the descriptor is attached.
            name: The name of the attribute.
        """
        self._attr = name

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
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError("Attribute not found")

    def __set__(self, obj: object, value: Any) -> None:
        """
        Set the attribute value, ensuring it is not a Python keyword.

        Args:
            obj: The instance of the class.
            value: The value to set.

        Raises:
            ValueError: If the value is a Python keyword string.
        """
        if self.__is_string_keyword(value):
            raise ValueError("Invalid value")
        obj.__dict__[self._attr] = value

    @staticmethod
    def __is_string_keyword(value: Any) -> bool:
        """
        Check if the value is a Python keyword string.

        Args:
            value: The value to check.

        Returns:
            bool: True if the value is a string and a Python keyword,
                  False otherwise.
        """
        return isinstance(value, str) and keyword.iskeyword(value)
