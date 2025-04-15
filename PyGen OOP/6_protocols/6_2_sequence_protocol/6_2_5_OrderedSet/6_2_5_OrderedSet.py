'''
TODO:
    Implement the OrderedSet class that describes an ordered set.

    When instantiating the class, it must accept one argument:
        iterable — an iterable object that defines the initial set of elements
                   of the ordered set.
                   If not passed, the initial set of elements is considered
                   empty

    The OrderedSet class must have two instance methods:
        add() — a method that takes an arbitrary object as an argument and
                adds it to the end of the ordered set
        discard() — a method that takes an arbitrary object as an argument
                    and removes it from the ordered set if it is present

    When passing an instance of the OrderedSet class to the len() function,
    the number of elements in it must be returned.

    In addition, an instance of the OrderedSet class must be an iterable
    object, that is, it must allow its elements to be iterated over,
    for example, using a for loop.

    Also, an instance of the OrderedSet class must support the membership
    operation using the 'in' operator.

    Finally, OrderedSet instances must support comparison operations using
    the '==' and '!=' operators.

    Methods implementing comparison operations must be able to compare
    two OrderedSet instances with each other, as well as an OrderedSet
    instance with a set instance.

    When an ordered set is compared to an ordered set, they are considered
    equal if they have the same length and contain equal elements in equal
    positions.

    When an ordered set is compared to a regular set, they are considered
    equal if they have the same length and contain equal elements, regardless
    of their position.

NOTE:
    An OrderedSet instance must be independent of the iterable from which
    it was created.

    In other words, if the original iterable changes, the OrderedSet instance
    must not change.

    If the object being compared is invalid, the method implementing
    the comparison operation must return the NotImplemented constant.

    There are no restrictions regarding the implementation of the OrderedSet
    class, it can be arbitrary.
'''
from typing import Any, Iterable, Iterator, Union


class OrderedSet:
    """
    An ordered set maintaining insertion order of unique elements.
    """

    def __init__(self, iterable: Iterable[Any] = ()) -> None:
        """
        Initialize with an iterable, preserving order and removing duplicates.

        Args:
            iterable: Initial elements (default is empty).
        """
        self._set = []
        for item in iterable:
            if item not in self._set:
                self._set.append(item)

    def add(self, obj: Any) -> None:
        """
        Add an object to the end if not already present.

        Args:
            obj: The object to add.
        """
        if obj not in self._set:
            self._set.append(obj)

    def discard(self, obj: Any) -> None:
        """
        Remove an object if present.

        Args:
            obj: The object to remove.
        """
        if obj in self._set:
            self._set.remove(obj)

    def __len__(self) -> int:
        """
        Return the number of elements.

        Returns:
            int: The number of unique elements.
        """
        return len(self._set)

    def __iter__(self) -> Iterator[Any]:
        """
        Yield elements in order of insertion.

        Yields:
            Any: Elements of the set.
        """
        yield from self._set

    def __contains__(self, obj: Any) -> bool:
        """
        Check if an object is in the set.

        Args:
            obj: The object to check.

        Returns:
            bool: True if the object is present, False otherwise.
        """
        return obj in self._set

    def __eq__(self, other: Any) -> Union[bool, type(NotImplemented)]:
        """
        Compare with another OrderedSet or set.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if equal, False otherwise.
            NotImplemented: If comparison is not supported.
        """
        if isinstance(other, OrderedSet):
            return self._set == list(other)
        if isinstance(other, set):
            return len(self._set) == len(other) and set(self._set) == other
        return NotImplemented
