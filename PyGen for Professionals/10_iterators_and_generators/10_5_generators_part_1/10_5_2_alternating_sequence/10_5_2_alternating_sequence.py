'''
TODO:
    Implement a generator function alternating_sequence() that takes
    one argument:
        - count is a natural number, defaulting to None

    If count is None, the function should return a generator that produces
    an infinite alternating sequence of natural numbers.

    If count is a natural number, the function should return a generator that
    produces the first count numbers in the alternating sequence of natural
    numbers, and then raises a StopIteration exception.

NOTE:
The alternating sequence of natural numbers is:
    1,-2,3,-4,5,-6,7,-8,9,-10,...
'''
from typing import Generator


def alternating_sequence(count: int = None) -> Generator[int, None, None]:
    """
    Generate an alternating sequence of natural numbers.

    If count is None, it generates an infinite sequence of alternating
    natural numbers. Otherwise, it generates the first 'count' numbers
    in the alternating sequence.

    Args:
        count (int, optional): The number of terms to generate.
                               Defaults to None.

    Yields:
        int: An alternating sequence of natural numbers.
    """
    def get_signed_number(number: int) -> int:
        """
        Get a number with alternating sign.

        Args:
            number (int): The number whose sign will be alternated.

        Returns:
            int: The number with the alternating sign.
        """
        return number if number % 2 else -number

    number = 1

    if count is None:
        # Infinite sequence
        while True:
            yield get_signed_number(number)
            number += 1
    else:
        # Finite sequence
        for _ in range(count):
            yield get_signed_number(number)
            number += 1
