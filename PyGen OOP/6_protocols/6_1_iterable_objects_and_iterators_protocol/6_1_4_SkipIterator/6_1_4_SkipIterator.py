'''
TODO:
    Implement the SkipIterator class.

    When instantiated, the class must accept two arguments in the following
    order:
        iterable — the iterable
        n — a non-negative integer

    An instance of the SkipIterator class must be an iterator that generates
    elements of the iterable, iterable, bypassing n elements, and then raises
    a StopIteration exception.

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with valid data.

    The SkipIterator class must satisfy the iterator protocol, that is,
    have __iter__() and __next__() methods.

    The protocol implementation is arbitrary.
'''
from typing import Any, Iterator, Iterable


class SkipIterator:
    """
    An iterator that skips n elements between each yielded element from
    an iterable.
    """

    def __init__(self, iterable: Iterable[Any], n: int) -> None:
        """
        Initialize the iterator with an iterable and skip count.

        Args:
            iterable: The iterable whose elements will be processed.
            n: Number of elements to skip between yielded elements.
        """
        self._iterator = iter(iterable)
        self._n = n

    def __iter__(self) -> Iterator[Any]:
        """
        Return the iterator object itself.

        Returns:
            Iterator: The iterator itself.
        """
        return self

    def __next__(self) -> Any:
        """
        Return the next element, skipping n elements.

        Returns:
            Any: The next element from the iterable.

        Raises:
            StopIteration: If there are no more elements to return.
        """
        result = next(self._iterator)

        for _ in range(self._n):
            try:
                next(self._iterator)
            except StopIteration:
                pass
        return result
