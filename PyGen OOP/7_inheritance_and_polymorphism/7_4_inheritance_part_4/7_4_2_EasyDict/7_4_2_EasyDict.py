'''
TODO:
    Implement the EasyDict class, a dict class inheritor, describing
    a dictionary whose element values can be retrieved both by keys ([key])
    and by the same-name attributes (.key).

    The process of creating an instance of the EasyDict class must coincide
    with the process of creating an instance of the dict class.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the EasyDict
    class, it can be arbitrary.
'''
from typing import Any


class EasyDict(dict):
    """
    Class representing a dictionary with attribute-style access to values.

    Inherits from dict, allowing values to be accessed via keys (d[key]) or
    attributes (d.key).
    """

    def __getattr__(self, attr: str) -> Any:
        """
        Get a value by attribute name, equivalent to dictionary key access.

        Args:
            attr: The attribute name (key) to access.

        Returns:
            Any: The value associated with the key.

        Raises:
            KeyError: If the key does not exist in the dictionary.
        """
        return self[attr]

    def __setattr__(self, attr: str, value: Any) -> None:
        """
        Set a value by attribute name, equivalent to dictionary key assignment.

        Args:
            attr: The attribute name (key) to set.
            value: The value to assign.
        """
        self[attr] = value

    def __delattr__(self, attr: str) -> None:
        """
        Delete a key-value pair by attribute name, equivalent to dictionary
        key deletion.

        Args:
            attr: The attribute name (key) to delete.

        Raises:
            KeyError: If the key does not exist in the dictionary.
        """
        del self[attr]
