'''
TODO:
    Implement a generator function reverse() that takes one argument:
        - sequence — a sequence

    The function should return a generator that produces the elements of
    sequence in reverse order and then raises a StopIteration exception.

NOTE:
    A sequence is a collection that supports indexing and has a length.

    For example, objects of type list, str, tuple are sequences.
'''
from typing import Sequence, Generator, Any


def reverse(sequence: Sequence[Any]) -> Generator[Any, None, None]:
    """
    Generate elements of the given sequence in reverse order.

    Args:
        sequence (Sequence[Any]): A sequence supporting indexing and length.

    Yields:
        Any: Elements of the sequence in reverse order.
    """
    yield from reversed(sequence)
