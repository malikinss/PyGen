'''
TODO:
    Implement the interleave() function using generator expressions that takes
    an arbitrary number of positional arguments, each of which is a sequence.

    The function must return a generator that produces each element of all
    the sequences passed in:
        first the first element of the first sequence, then the first element
        of the second sequence, and so on;
        then the second element of the first sequence, then the second element
        of the second sequence, and so on.

NOTE:
    A sequence is a collection that supports indexing and has a length.

    For example, list, str, tuple are sequences.

    It is guaranteed that all sequences passed to the function have equal
    lengths.

    It is guaranteed that at least one sequence is always passed to
    the function.
'''
from typing import Sequence, Any, Generator


def interleave(*args: Sequence[Any]) -> Generator[Any, None, None]:
    """
    Returns a generator that produces elements from multiple sequences in
    an interleaved order.

    Args:
        *args (Sequence[Any]): An arbitrary number of sequences
        (lists, tuples, strings, etc.) with equal lengths.

    Returns:
        Generator[Any, None, None]: A generator that yields elements in the
        interleaved order.

    Example:
        list(
            interleave([1, 2], 'ab', (True, False))
        ) -> [1, 'a', True, 2, 'b', False]
    """
    return (element for group in zip(*args) for element in group)
