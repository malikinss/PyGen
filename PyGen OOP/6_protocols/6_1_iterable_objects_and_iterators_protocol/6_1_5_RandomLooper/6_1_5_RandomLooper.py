'''
TODO:
    Implement the RandomLooper class.

    When instantiated, the class must accept an arbitrary number of positional
    arguments, each of which is an iterable.

    An instance of the RandomLooper class must be an iterator that randomly
    generates all elements of all iterables passed to the constructor,
    and then raises a StopIteration exception.

NOTE:
    The order of the elements in the returned iterator does not have to match
    their order in the test data.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    The RandomLooper class must satisfy the iterator protocol, that is,
    have __iter__() and __next__() methods.

    The protocol implementation is arbitrary.
'''
from typing import Any, Iterator, Iterable
from random import choice


class RandomLooper:
    """
    An iterator that randomly yields elements from multiple iterables.
    """

    def __init__(self, *args: Iterable[Any]) -> None:
        """
        Initialize the iterator with iterables.

        Args:
            *args: Variable number of iterables whose elements will be yielded
            randomly.
        """
        self._iterators = [iter(iterable) for iterable in args]
        self._elements = []

    def __iter__(self) -> Iterator[Any]:
        """
        Return the iterator object itself.

        Returns:
            Iterator: The iterator itself.
        """
        return self

    def __next__(self) -> Any:
        """
        Return a random element from the iterables.

        Returns:
            Any: A randomly selected element.

        Raises:
            StopIteration: If all iterables are exhausted.
        """
        while self._elements or self._iterators:
            if not self._elements:
                for i in range(len(self._iterators) - 1, -1, -1):
                    try:
                        self._elements.append(next(self._iterators[i]))
                    except StopIteration:
                        self._iterators.pop(i)
            if self._elements:
                return self._elements.pop(choice(range(len(self._elements))))
        raise StopIteration
