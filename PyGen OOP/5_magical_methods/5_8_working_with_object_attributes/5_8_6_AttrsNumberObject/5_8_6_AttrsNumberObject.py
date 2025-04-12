'''
TODO:
    Implement the AttrsNumberObject class.

    When creating an instance, the class must accept an arbitrary number of
    named arguments.

    All arguments passed must be set as attributes of the created instance.

    An instance of the AttrsNumberObject class must have one attribute:
        attrs_num — the number of attributes that the instance of
                    the AttrsNumberObject class currently has, including
                    the attrs_num attribute itself

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the AttrsNumberObject class, it can be arbitrary.
'''
from typing import Any


class AttrsNumberObject:
    """
    A class that tracks the number of its attributes.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize with arbitrary named attributes.

        Args:
            **kwargs: Named arguments to set as attributes.
        """
        object.__setattr__(self, 'attrs_num', 1)
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)
            self._update_attrs_num()

    def __setattr__(self, attr: str, value: Any) -> None:
        """Set an attribute and update attrs_num.

        Args:
            attr (str): The name of the attribute.
            value (Any): The value to set.
        """
        object.__setattr__(self, attr, value)
        self._update_attrs_num()

    def __delattr__(self, attr: str) -> None:
        """Delete an attribute and update attrs_num.

        Args:
            attr (str): The name of the attribute to delete.
        """
        object.__delattr__(self, attr)
        self._update_attrs_num()

    def _update_attrs_num(self) -> None:
        """
        Update attrs_num to reflect the current number of attributes.
        """
        object.__setattr__(self, 'attrs_num', len(self.__dict__))
