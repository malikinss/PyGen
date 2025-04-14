'''
TODO:
    A sparse array (list) is an abstract representation of a regular
    array (list) in which the data is not presented continuously,
    but fragmentarily:
        most of its elements take the same default value, usually 0 or None.

    In a sparse array, it is possible to access undefined elements, in which'
    case the array will return some default value.

    Implement the SparseArray class, which describes a sparse array.

    When creating an instance, the class must accept one argument:
        default — the default value for undefined elements of the sparse array

    An instance of the SparseArray class must allow getting and changing
    the values of its elements using indices.

    When trying to get the value of an element by a non-existent index,
    the default value must be returned.

NOTE:
    It is guaranteed that only non-negative indices are used when accessing
    elements.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the SparseArray
    class, it can be arbitrary.
'''
from typing import Any


class SparseArray:
    """
    A sparse array storing only non-default elements.
    """

    def __init__(self, default: Any) -> None:
        """
        Initialize the sparse array with a default value.

        Args:
            default: The value returned for undefined indices.
        """
        self.default = default
        self._data = {}  # Dictionary to store index: value pairs

    def __getitem__(self, key: int) -> Any:
        """
        Get the value at the given index.

        Args:
            key: The index to access.

        Returns:
            Any: The value at the index, or default if undefined.
        """
        return self._data.get(key, self.default)

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Set the value at the given index.

        Args:
            key: The index to set.
            value: The value to assign.
        """
        if value == self.default:
            self._data.pop(key, None)  # Remove key if value is default
        else:
            self._data[key] = value
