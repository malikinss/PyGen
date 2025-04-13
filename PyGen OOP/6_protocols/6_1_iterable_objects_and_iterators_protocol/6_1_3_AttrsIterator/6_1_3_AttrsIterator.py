'''
TODO:
    Implement the AttrsIterator class.

    When instantiated, the class must accept one argument:
        obj — an arbitrary object

    An instance of the AttrsIterator class must be an iterator that generates
    all attributes of the obj object as tuples of two elements, the first of
    which represents the attribute name, and the second — the attribute value.

NOTE:
    The order of attributes during generation must match their order in
    the attribute dictionary __dict__.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    The AttrsIterator class must satisfy the iterator protocol, that is, have
    the __iter__() and __next__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Any, Iterator, Tuple


class AttrsIterator:
    """
    An iterator over the attributes of an object as name-value tuples.
    """

    def __init__(self, obj: Any) -> None:
        """
        Initialize the iterator with an object's attributes.

        Args:
            obj: The object whose attributes will be iterated over.
        """
        self._pairs = list(obj.__dict__.items())
        self._index = 0

    def __iter__(self) -> Iterator[Tuple[str, Any]]:
        """
        Return the iterator object itself.

        Returns:
            Iterator: The iterator itself.
        """
        return self

    def __next__(self) -> Tuple[str, Any]:
        """
        Return the next attribute name-value tuple.

        Returns:
            Tuple[str, Any]: A tuple of (attribute_name, attribute_value).

        Raises:
            StopIteration: If there are no more attributes to return.
        """
        if self._index >= len(self._pairs):
            raise StopIteration
        result = self._pairs[self._index]
        self._index += 1
        return result
