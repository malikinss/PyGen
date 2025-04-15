'''
TODO:
    Implement the SequenceZip class.

    When instantiated, the class must accept an arbitrary number of positional
    arguments, each of which is a sequence.

    The SequenceZip class must describe a sequence whose elements are
    the elements of the iterables passed to the constructor, combined into
    tuples.

    The combination must be similar to that of the zip() function.

    When passed to the len() function, the number of elements in
    the SequenceZip instance must be returned.

    Also, the SequenceZip instance must be an iterable object, i.e., it must
    allow its elements to be iterated over, for example, using a for loop.

    Finally, the SequenceZip instance must allow the values of its elements to
    be retrieved using indices.

NOTE:
    Elements are guaranteed to be accessed using only non-negative indices.

    The SequenceZip instance must be independent of the sequences from which
    it was instantiated.

    In other words, if the original sequences change, the instance of
    the SequenceZip class should not change.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the SequenceZip
    class, it can be arbitrary.
'''
from typing import Any, Iterable, Sequence, Tuple


class SequenceZip:
    """
    A memory-efficient sequence of tuples combining elements from multiple
    sequences.
    """

    def __init__(self, *args: Sequence[Any]) -> None:
        """
        Initialize with sequences to zip.

        Args:
            *args: Sequences to combine into tuples.
        """
        self._sequences = [tuple(seq) for seq in args]

    def __len__(self) -> int:
        """
        Return the number of zipped tuples.

        Returns:
            int: The length of the shortest input sequence.
        """
        return min((len(seq) for seq in self._sequences), default=0)

    def __iter__(self) -> Iterable[Tuple[Any, ...]]:
        """
        Yield zipped tuples.

        Yields:
            Tuple[Any, ...]: Tuples combining elements from input sequences.
        """
        yield from zip(*self._sequences)

    def __getitem__(self, key: int) -> Tuple[Any, ...]:
        """
        Get a zipped tuple by index.

        Args:
            key: The index of the tuple.

        Returns:
            Tuple[Any, ...]: The tuple at the given index.

        Raises:
            IndexError: If the index is out of range.
        """
        return tuple(seq[key] for seq in self._sequences)
