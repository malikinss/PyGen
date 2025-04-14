'''
TODO:
    Implement the ReversedSequence class, which describes an object that
    implements access to elements of some sequence in reverse order.

    When creating an instance, the class must accept one argument:
        sequence — a sequence

    When passing an instance of the ReversedSequence class to
    the len() function, its length must be returned, represented by the number
    of elements in the original sequence.

    Also, an instance of the ReversedSequence class must be an iterable object
    whose elements are the elements of the original sequence in reverse order.

    Finally, an instance of the ReversedSequence class must allow obtaining
    the values of the elements of the original sequence using indices,
    and the indexing must be performed in reverse order, that is, the last
    element of the original sequence must be accessible at index 0,
    the penultimate element at index 1, the penultimate element at index 2,
    and so on.

NOTE:
    It is guaranteed that only non-negative indices are used when accessing
    elements.

    An instance of the ReversedSequence class must depend on the sequence
    it was created on.

    In other words, if the original sequence changes, then the instance of
    the ReversedSequence class must change as well.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the ReversedSequence class, it can be arbitrary.
'''


from typing import Any, Iterable, Sequence


class ReversedSequence:
    """
    An iterable object providing reversed access to a sequence.
    """

    def __init__(self, sequence: Sequence[Any]) -> None:
        """
        Initialize with a sequence.

        Args:
            sequence: The sequence to access in reverse order.
        """
        self.sequence = sequence

    def __len__(self) -> int:
        """
        Return the length of the sequence.

        Returns:
            int: The number of elements in the sequence.
        """
        return len(self.sequence)

    def __iter__(self) -> Iterable[Any]:
        """
        Yield elements of the sequence in reverse order.

        Yields:
            Any: Elements of the sequence in reverse order.
        """
        yield from reversed(self.sequence)

    def __getitem__(self, key: Any) -> Any:
        """
        Access elements of the sequence by index in reverse order.

        Args:
            key: The index (non-negative integer).

        Returns:
            Any: The element at the reversed index.

        Raises:
            TypeError: If the key is not an integer.
            IndexError: If the index is out of range.
        """
        if not isinstance(key, int):
            raise TypeError("Index must be an integer")
        return self.sequence[-key - 1]
