'''
TODO:
    Implement the LoopTracker class.

    When instantiated, the class must accept one argument:
        iterable — the iterable

    An instance of the LoopTracker class must be an iterator that emits
    the elements of the iterable in the original order, and then throws
    a StopIteration exception.

    The LoopTracker class must have four properties:
        - accesses — a read-only property that returns the number of elements
                     the iterator has emitted so far
        - empty_accesses — a read-only property that returns the number of
                           attempts to get the next element of an empty
                           iterator
        - first — a read-only property that returns the first element of
                  the iterator and does not shift it.
                  If the iterator does not have a first element,
                  i.e. is created based on an empty iterable, then
                  an AttributeError exception should be raised with the text:
                    The original iterable is empty
        - last — a read-only property that returns the last element generated
                 by the iterator so far.
                 If the iterator has not generated any elements yet, then
                 an AttributeError exception should be raised with the text:
                    There is no last element

    The LoopTracker class should have one instance method:
        - is_empty() — a method that returns True if the iterator is empty,
                       or False otherwise

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    The LoopTracker class must satisfy the iterator protocol, i.e. have
    the __iter__() and __next__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Any, Iterator, Iterable


class LoopTracker:
    """
    An iterator that tracks accesses, empty accesses, first, and last elements.
    """

    def __init__(self, iterable: Iterable[Any]) -> None:
        """
        Initialize the iterator with an iterable.

        Args:
            iterable: The iterable whose elements will be yielded.
        """
        self._iterator = iter(iterable)
        self._next_item = None
        self._first_item = None
        self._last_item = None
        self._has_item = False
        self._access_count = 0
        self._empty_calls = 0

        # Try to load the first element
        try:
            self._next_item = next(self._iterator)
            self._first_item = self._next_item
            self._has_item = True
        except StopIteration:
            self._has_item = False

    def __iter__(self) -> Iterator[Any]:
        """
        Return the iterator object itself.

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
            self._empty_calls += 1
            raise StopIteration

        result = self._next_item
        self._last_item = self._next_item
        self._access_count += 1

        try:
            self._next_item = next(self._iterator)
        except StopIteration:
            self._has_item = False
            self._next_item = None
        return result

    @property
    def accesses(self) -> int:
        """
        Return the number of elements emitted by the iterator.

        Returns:
            int: The number of elements returned by __next__.
        """
        return self._access_count

    @property
    def empty_accesses(self) -> int:
        """
        Return the number of attempts to access an empty iterator.

        Returns:
            int: The number of times __next__ was called after exhaustion.
        """
        return self._empty_calls

    @property
    def first(self) -> Any:
        """
        Return the first element of the iterator without advancing.

        Returns:
            Any: The first element.

        Raises:
            AttributeError: If the original iterable is empty.
        """
        if self._first_item is None:
            raise AttributeError("The original iterable is empty")
        return self._first_item

    @property
    def last(self) -> Any:
        """
        Return the last element emitted by the iterator.

        Returns:
            Any: The last element emitted.

        Raises:
            AttributeError: If no elements have been emitted yet.
        """
        if self._last_item is None:
            raise AttributeError("There is no last element")
        return self._last_item

    def is_empty(self) -> bool:
        """
        Return whether the iterator is empty.

        Returns:
            bool: True if the iterator is empty, False otherwise.
        """
        return not self._has_item
