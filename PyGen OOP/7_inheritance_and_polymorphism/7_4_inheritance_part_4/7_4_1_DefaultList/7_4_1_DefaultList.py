'''
TODO:
    Implement a DefaultList class that inherits from UserList and describes
    a list that returns a default value when attempting to get an element at
    a non-existent index.

    When instantiating, the class must accept two arguments in the following
    order:
        iterable — an iterable that defines the initial set of elements of
                   the DefaultList instance.
                   If not passed, the initial set of elements is considered
                   empty
        default — the value returned when attempting to get an element at
                  a non-existent index.
                  Defaults to None

NOTE:
    An instance of the DefaultList class must not depend on the iterable it
    was created on.

    In other words, if the original iterable changes, the DefaultList instance
    must not change.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the DefaultList
    class, it can be arbitrary.
'''
from collections import UserList
from collections.abc import Iterable
from typing import Any


class DefaultList(UserList):
    """
    Class representing a list that returns a default value for non-existent
    indices.

    Inherits from UserList, with a default value returned when accessing
    out-of-bounds indices.
    """

    def __init__(
        self, iterable: Iterable[Any] = (), default: Any = None
    ) -> None:
        """
        Initialize a DefaultList with elements from iterable and a default
        value.

        Args:
            iterable: An iterable defining the initial elements.
                      Defaults to an empty tuple.
            default: The value returned for non-existent indices.
                     Defaults to None.
        """
        self._default = default
        super().__init__(iterable)

    def __getitem__(self, index: int) -> Any:
        """
        Return the element at the given index or the default value if index
        is out of bounds.

        Args:
            index: The index to access.

        Returns:
            Any: The element at the index or the default value if the index
                 does not exist.
        """
        try:
            return self.data[index]
        except IndexError:
            return self._default
