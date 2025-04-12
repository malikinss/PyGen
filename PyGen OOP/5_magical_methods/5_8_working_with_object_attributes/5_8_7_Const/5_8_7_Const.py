'''
TODO:
    Implement the Const class.

    When creating an instance, the class must accept an arbitrary number
    of named arguments.

    All arguments passed must be set as attributes of the instance being
    .

    The Const class must allow attributes to be set and retrieved for its
    instances, but must not allow values of these attributes to be changed or
    deleted.

    When attempting to change the value of an attribute, an AttributeError
    exception must be raised with the text:
        Changing the attribute value is not allowed

    When attempting to delete an attribute, an AttributeError exception must
    be raised with the text:
        Deleting the attribute is not allowed

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Const class,
    it can be arbitrary.
'''
from typing import Any


class Const:
    """
    A class with immutable attributes set during initialization.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize with arbitrary named attributes.

        Args:
            **kwargs: Named arguments to set as attributes.
        """
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)

    def __setattr__(self, attr: str, value: Any) -> None:
        """
        Prevent changing existing attributes.

        Args:
            attr (str): The name of the attribute.
            value (Any): The value to set.

        Raises:
            AttributeError: If attempting to change an existing attribute.
        """
        if hasattr(self, attr):
            raise AttributeError("Changing the attribute value is not allowed")
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr: str) -> None:
        """
        Prevent deleting attributes.

        Args:
            attr (str): The name of the attribute.

        Raises:
            AttributeError: If attempting to delete an attribute.
        """
        raise AttributeError("Deleting the attribute is not allowed")
