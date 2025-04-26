'''
TODO:
    Implement a SortedList class that describes a list that is automatically
    sorted on creation and any modification.

    When instantiated, the class must accept one argument:
        iterable — an iterable that defines the initial set of elements of
                   the sorted list.
                   If not passed, the initial set of elements is considered
                   empty

    The SortedList class must have three instance methods:
        add() — a method that takes an arbitrary object as an argument and
                adds it to the SortedList instance
        discard() - a method that takes an arbitrary object as an argument and
                    removes all of its entries from the SortedList instance if
                    it is present.
        update() — a method that takes an iterable as an argument and adds all
                   of its elements to the SortedList instance

    The SortedList class must also have instance methods such as append(),
    insert(), extend(), and reverse(), which must throw a NotImplementedError
    exception when used.

    A SortedList instance must have the following formal string representation:
        SortedList(
            [<first element of the list>, <second element of the list>, ...]
        )

    When passing a SortedList instance to the len() function, the number of
    elements in it must be returned.

    A NotImplementedError exception must be raised when attempting to pass
    a SortedList instance to the reversed() function.

    In addition, a SortedList instance must be an iterable object,
    i.e. it must allow its elements to be iterated over, for example, using
    a for loop.

    Also, a SortedList instance must support the membership check operation
    using the in operator.

    In addition, a SortedList instance must allow its elements to be retrieved
    and deleted using indices, both positive and negative.

    A NotImplementedError exception must be raised when attempting to change
    the value of an element by its index.

    Instances of the SortedList class must support arithmetic operations
    between themselves using the + and += operators:
        the + operator - must perform the operation of adding two sorted lists
                         by concatenating them and then sorting them.
                         The result of the operator must be a new instance of
                         the SortedList class
        the += operator - must perform the operation of adding two sorted
                          lists by concatenating them and then sorting them.
                          The result of the operator must be the left instance
                          of the SortedList class

    Finally, an instance of the SortedList class must support the operation of
    multiplying by an integer n using the * and *= operators:
        the * operator - must perform the operation of multiplying a sorted
                         list by a number and then sorting it.
                         The result of the operator must be a new instance of
                         the SortedList class
        the *= operator - must perform the operation of multiplying a sorted
                          list by a number and then sorting it.
                          The result of the operator must be the left instance
                          of the SortedList class

NOTE:
    It is guaranteed that the elements of one instance of the SortedList class
    are objects that are comparable to each other.

    Before solving, think about which abstract class from the collections.abc
    module would be convenient as a parent.

    An instance of the SortedList class should not depend on the iterable
    object on which it was created.

    In other words, if the original iterable object changes, then the instance
    of the SortedList class should not change.

    If the object with which the arithmetic operation is performed is
    incorrect, the method implementing the comparison operation must return
    the NotImplemented constant.

    There are no restrictions regarding the implementation of the SortedList
    class, it can be arbitrary.

    However, try to solve the problem so that the operation of adding elements
    to the list is performed as quickly as possible.
'''
from collections.abc import Sequence, Iterable
from typing import Any, Union
import bisect


class SortedList(Sequence):
    """
    A sorted list that maintains order on creation and modification.

    Inherits from Sequence, supporting iteration, indexing, and arithmetic
    operations.
    """

    def __init__(self, iterable: Iterable[Any] = ()) -> None:
        """
        Initialize with sorted elements from iterable.

        Args:
            iterable: Iterable of comparable elements. Defaults to empty.
        """
        self._data = sorted(list(iterable))

    def add(self, obj: Any) -> None:
        """
        Add an object and maintain sort order.

        Args:
            obj: Object to add.
        """
        bisect.insort(self._data, obj)

    def discard(self, obj: Any) -> None:
        """
        Remove all occurrences of an object.

        Args:
            obj: Object to remove.
        """
        self._data[:] = [x for x in self._data if x != obj]

    def update(self, iterable: Iterable[Any]) -> None:
        """
        Add elements from iterable and maintain sort order.

        Args:
            iterable: Iterable of elements to add.
        """
        for item in iterable:
            bisect.insort(self._data, item)

    def append(self, value) -> None:
        """
        Not implemented for SortedList.
        """
        raise NotImplementedError

    def insert(self, key, value) -> None:
        """
        Not implemented for SortedList.
        """
        raise NotImplementedError

    def extend(self, iterable) -> None:
        """
        Not implemented for SortedList.
        """
        raise NotImplementedError

    def reverse(self) -> None:
        """
        Not implemented for SortedList.
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        """
        Return formal string representation.

        Returns:
            str: SortedList([...]).
        """
        return f"{self.__class__.__name__}({self._data})"

    def __len__(self) -> int:
        """
        Return number of elements.

        Returns:
            int: Length of the list.
        """
        return len(self._data)

    def __iter__(self) -> Iterable[Any]:
        """
        Iterate over elements.

        Returns:
            Iterable[Any]: Iterator of elements.
        """
        return iter(self._data)

    def __reversed__(self) -> None:
        """
        Not implemented for SortedList.
        """
        raise NotImplementedError

    def __getitem__(self, key: Union[int, slice]) -> Any:
        """
        Access element(s) by index or slice.

        Args:
            key: Index or slice.

        Returns:
            Any: Element or slice of elements.
        """
        return self._data[key]

    def __contains__(self, value: Any) -> bool:
        """
        Check if value is in the list.

        Args:
            value: Value to check.

        Returns:
            bool: True if value is present.
        """
        return value in self._data

    def __setitem__(self, key: Union[int, slice], value: Any) -> None:
        """
        Not implemented for SortedList.
        """
        raise NotImplementedError

    def __delitem__(self, key: Union[int, slice]) -> None:
        """Delete element(s) by index or slice.

        Args:
            key: Index or slice to delete.
        """
        del self._data[key]

    def __add__(self, other: Any) -> 'SortedList':
        """
        Concatenate with another SortedList and sort.

        Args:
            other: SortedList to concatenate.

        Returns:
            SortedList: New sorted list, or NotImplemented.
        """
        if not isinstance(other, SortedList):
            return NotImplemented
        return SortedList(self._data + other._data)

    def __iadd__(self, other: Any) -> 'SortedList':
        """
        Concatenate in-place with another SortedList and sort.

        Args:
            other: SortedList to concatenate.

        Returns:
            SortedList: Modified self, or NotImplemented.
        """
        if not isinstance(other, SortedList):
            return NotImplemented
        self.update(other._data)
        return self

    def __mul__(self, n: Any) -> 'SortedList':
        """
        Multiply list by an integer and sort.

        Args:
            n: Integer to multiply by.

        Returns:
            SortedList: New sorted list, or NotImplemented.
        """
        if not isinstance(n, int):
            return NotImplemented
        return SortedList(self._data * n)

    def __imul__(self, n: Any) -> 'SortedList':
        """
        Multiply list in-place by an integer and sort.

        Args:
            n: Integer to multiply by.

        Returns:
            SortedList: Modified self, or NotImplemented.
        """
        if not isinstance(n, int):
            return NotImplemented
        self._data *= n
        self._data[:] = sorted(self._data)
        return self
