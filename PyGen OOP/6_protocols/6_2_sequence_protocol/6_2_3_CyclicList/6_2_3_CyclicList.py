'''
TODO:
    Implement a CyclicList class that describes a cyclic list.

    When instantiated, the class must accept one argument:
        iterable — an iterable that defines the initial set of elements of
                   the cyclic list.

    If not passed, the initial set of elements is considered empty

    The CyclicList class must have two instance methods:
        append() — a method that takes an arbitrary object as an argument and
                   adds it to the end of the cyclic list
        pop() — a method that takes an index of an element of the cyclic list
                as an argument, returns its value, and removes the element
                with the given index from the cyclic list.
                If no argument is passed, the last element of the cyclic list
                is considered to be the returned and removed element

    When passing an instance of the CyclicList class to the len() function,
    the number of elements in it must be returned.

    Also, an instance of the CyclicList class must be a cyclic iterable.

    In other words, it must be iterated over infinitely, and each time
    its last element is reached, it must start over.

    Finally, an instance of the CyclicList class must allow the values of
    its elements to be retrieved using indices, and the indices must work
    cyclically.

    For example, in the cyclic list [1, 2, 3], the element with index 4 must
    be the number 2.

NOTE:
    It is guaranteed that only non-negative indices are used when accessing
    elements.

    An instance of the CyclicList class must not depend on the iterable object
    from which it was created.

    In other words, if the original iterable object changes, then the instance
    of the CyclicList class must not change.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the CyclicList class, it can be arbitrary.
'''
from typing import Any, Iterable, Iterator, Optional


class CyclicList:
    """
    A cyclic list supporting infinite iteration and cyclic indexing.
    """

    def __init__(self, iterable: Iterable[Any] = ()) -> None:
        """
        Initialize the cyclic list with an iterable.

        Args:
            iterable: Initial elements of the list (default is empty).
        """
        self._list = list(iterable)

    def append(self, obj: Any) -> None:
        """
        Add an object to the end of the list.

        Args:
            obj: The object to append.
        """
        self._list.append(obj)

    def pop(self, id: Optional[int] = None) -> Any:
        """
        Remove and return an element at the given index.

        Args:
            id: The index of the element to remove (default is None, removes
                last element).

        Returns:
            Any: The removed element.

        Raises:
            IndexError: If the list is empty or index is out of range.
        """
        if id is None:
            return self._list.pop()
        return self._list.pop(id)

    def __len__(self) -> int:
        """
        Return the number of elements in the list.

        Returns:
            int: The number of elements.
        """
        return len(self._list)

    def __iter__(self) -> Iterator[Any]:
        """
        Yield elements infinitely in a cyclic manner.

        Yields:
            Any: Elements of the list, repeating indefinitely.
        """
        if not self._list:
            return
        while True:
            for item in self._list:
                yield item

    def __getitem__(self, key: int) -> Any:
        """
        Get an element by index, cyclically.

        Args:
            key: The index (non-negative integer).

        Returns:
            Any: The element at the cyclic index.

        Raises:
            IndexError: If the list is empty.
        """
        if not self._list:
            raise IndexError("CyclicList is empty")
        return self._list[key % len(self._list)]
