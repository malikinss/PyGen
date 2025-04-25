'''
TODO:
    Implement a TwoWayDict class, a subclass of UserDict, that describes
    a bidirectional dictionary where each time a key:value pair is added,
    the value:key pair is also added.

    The process of creating an instance of the TwoWayDict class must coincide
    with the process of creating an instance of the UserDict class.

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the TwoWayDict
    class, it can be arbitrary.
'''
from collections import UserDict
from typing import Any


class TwoWayDict(UserDict):
    """
    Class representing a bidirectional dictionary.

    Inherits from UserDict, adding value:key pair whenever a key:value pair
    is added.
    """
    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Add a key:value pair and its reverse value:key pair.

        Args:
            key: The key to add.
            value: The value to add.
        """
        # Add new pairs
        self.data[key] = value
        self.data[value] = key
