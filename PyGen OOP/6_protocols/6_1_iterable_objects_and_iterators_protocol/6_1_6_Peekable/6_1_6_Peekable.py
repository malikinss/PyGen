'''
TODO:
    Implement the Peekable class.

    When instantiated, the class must accept one argument:
        iterable — the iterable

    An instance of the Peekable class must be an iterator that emits
    the elements of the iterable in the original order, and then raises
    a StopIteration exception.

    The Peekable class must have one instance method:
        peek() — a method that returns the next element of the iterator,
                 similar to the next() function, but does not advance
                 the iterator.

    If the iterator is empty, a StopIteration exception must be raised.

    The method must also be able to accept one optional argument:
        default — an object that will be returned instead of raising
                  a StopIteration exception if the iterator is empty

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with valid data.

    The Peekable class must conform to the iterator protocol, that is, it must
    have __iter__() and __next__() methods.

    The implementation of the protocol can be arbitrary.
'''
from typing import Any, Iterator, Iterable, Optional


class Peekable:
    """
    An iterator that allows peeking at the next element without advancing.
    """
    _SENTINEL = object()  # Unique marker for default argument

    def __init__(self, iterable: Iterable[Any]) -> None:
        """
        Initialize the iterator with an iterable.

        Args:
            iterable: The iterable whose elements will be yielded.
        """
        self._iterator = iter(iterable)
        self._next_item = None
        self._has_item = False

        # Try to load the first element
        try:
            self._next_item = next(self._iterator)
            self._has_item = True
        except StopIteration:
            self._has_item = False

    def __iter__(self) -> Iterator[Any]:
        """Return the iterator object itself.

        Returns:
            Iterator: The iterator itself.
        """
        return self

    def __next__(self) -> Any:
        """
        Return the next element and advance the iterator.

        Returns:
            Any: The next element.

        Raises:
            StopIteration: If there are no more elements.
        """
        if not self._has_item:
            raise StopIteration
        result = self._next_item
        try:
            self._next_item = next(self._iterator)
        except StopIteration:
            self._has_item = False
            self._next_item = None
        return result

    def peek(self, default: Optional[Any] = _SENTINEL) -> Any:
        """
        Return the next element without advancing the iterator.

        Args:
            default: Value to return if the iterator is exhausted (optional).

        Returns:
            Any: The next element, or default if the iterator is empty.

        Raises:
            StopIteration: If the iterator is empty and no default is provided.
        """
        if self._has_item:
            return self._next_item
        if default is self._SENTINEL:
            raise StopIteration
        return default
