'''
TODO:
    Implement the DefaultObject class.

    When creating an instance, the class must accept one named argument
    default, which has a default value of None, and then an arbitrary number
    of named arguments.

    Arguments passed after default must be set as attributes of the created
    instance.

    When accessing a non-existent attribute of an instance of
    the DefaultObject class, the default value must be returned.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the DefaultObject class, it can be arbitrary.
'''
from typing import Any


class DefaultObject:
    """
    A class that stores attributes and returns a default value for missing
    ones.
    """

    def __init__(self, default: Any = None, **kwargs: Any) -> None:
        """
        Initialize with a default value and arbitrary named attributes.

        Args:
            default (Any, optional): The value to return for missing
                                     attributes. Defaults to None.
            **kwargs: Arbitrary named arguments to set as attributes.
        """
        object.__setattr__(self, 'default', default)
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)

    def __getattr__(self, attr: str) -> Any:
        """
        Return the default value for non-existent attributes.

        Args:
            attr (str): The name of the attribute.

        Returns:
            Any: The default value specified during initialization.
        """
        return object.__getattribute__(self, 'default')
