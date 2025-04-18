'''
TODO:
    Implement the Atomic class.

    When instantiated, the class must accept two arguments in the following
    order:
        data — an arbitrary list, set, or dictionary
        deep — a boolean value, defaults to False

    An instance of the Atomic class must be a context manager that allows
    operations on the data collection inside the with block to be performed
    atomically, that is, either all operations must be performed or none of
    them.

    If all operations are correct (do not result in an exception being thrown),
    they must be applied to the data collection.

    If any operation is incorrect, all previously performed operations must
    be undone, and the data collection must be reset.

    The deep parameter must determine the state of the nested structures of
    the data collection after the with block has completed.

    If it is False, the context manager must reset only the data collection
    itself, without affecting its nested structures.

    For example, if data is a two-dimensional list and one of its nested lists
    is modified inside the with block, then this nested list must preserve its
    new state, even if subsequent operations inside the with block result in
    an exception being raised and the data collection being returned to its
    original state.

    If the deep parameter is True, the context manager must return not only
    the data collection itself, but also its nested structures to their
    original state.

NOTE:
    Visual examples of using the Atomic class are demonstrated in the test
    data.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    The Atomic class must satisfy the context manager protocol, that is,
    have the __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Optional, Type, Union
from types import TracebackType
from copy import copy, deepcopy


class Atomic:
    """
    A context manager for atomic operations on a list, set, or dictionary.
    """

    def __init__(
        self, data: Union[list, set, dict], deep: bool = False
    ) -> None:
        """
        Initialize with a data collection and a flag for deep copying.

        Args:
            data: A list, set, or dictionary to operate on.
            deep: Whether to perform a deep copy of nested structures.
                  Defaults to False.
        """
        self._data = data
        self._deep = deep
        self._copy = deepcopy(data) if deep else copy(data)

    def __enter__(self) -> Union[list, set, dict]:
        """
        Enter the context manager, returning a copy of the data.

        Returns:
            Union[list, set, dict]: A copy of the data collection
                                    for modifications.
        """
        return self._copy

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> bool:
        """
        Exit the context manager, applying or discarding changes based
        on exceptions.

        Args:
            exc_type: Type of the exception, or None if no exception occurred.
            exc_value: The exception instance, or None.
            traceback: The traceback object, or None.

        Returns:
            bool: True if an exception was suppressed, False otherwise.
        """
        if exc_type is not None:
            return True  # Suppress exception, discard changes
        # Apply changes from copy to original data
        if isinstance(self._data, list):
            self._data[:] = self._copy
        else:  # set or dict
            self._data.clear()
            self._data.update(self._copy)
        return False
