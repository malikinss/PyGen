'''
TODO:
    Implement a function alnum_sequence() that takes no arguments.

    The function should return an iterator that cyclically generates an
    infinite sequence of natural numbers and uppercase Latin letters:
        1,A,2,B,3,C,..,X,25,Y,26,Z
'''
from itertools import cycle
from collections.abc import Iterator


def alnum_sequence() -> Iterator[str | int]:
    """
    Generates an infinite sequence of natural numbers and uppercase Latin
    letters in a cyclic order:
        1, A, 2, B, 3, C, ..., 25, Y, 26, Z, 1, A, 2, B, ...

    Yields:
        Iterator[str | int]: Alternating numbers and letters.

    Example:
        >>> seq = alnum_sequence()
        >>> [next(seq) for _ in range(10)]
        [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
    """
    numbers = cycle(range(1, 27))
    letters = cycle(map(chr, range(65, 91)))

    yield from (
        val for pair in zip(numbers, letters) for val in pair
    )
