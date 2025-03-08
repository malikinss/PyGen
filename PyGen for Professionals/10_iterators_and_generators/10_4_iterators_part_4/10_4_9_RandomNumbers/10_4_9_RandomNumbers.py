'''
TODO:
    Implement a RandomNumbers class that produces iterators whose constructor
    takes three arguments in the following order:
        left - an integer
        right - an integer
        n - a natural number

    The iterator of class RandomNumbers must generate a sequence of n random
    numbers from left to right inclusive, and then raise a StopIteration
    exception.

NOTE:
    It is guaranteed that left <= right.
'''
import random
from typing import Iterator


class RandomNumbers:
    """
    Iterator that generates a sequence of 'n' random numbers
    in the range [left, right] inclusive.

    Once 'n' numbers are generated, raises StopIteration.

    Attributes:
        left (int): Lower bound (inclusive).
        right (int): Upper bound (inclusive).
        n (int): Number of random values to generate.
        _count (int): Counter to track generated numbers.
    """

    def __init__(self, left: int, right: int, n: int):
        """
        Initializes the RandomNumbers iterator.

        Args:
            left (int): Lower bound (inclusive).
            right (int): Upper bound (inclusive).
            n (int): Number of random values to generate.

        Raises:
            ValueError: If `left > right`.
            ValueError: If `n` is not a positive integer.
        """
        if left > right:
            raise ValueError("Left should be less than or equal to Right")
        if n <= 0:
            raise ValueError("n must be a positive integer")

        self.left = left
        self.right = right
        self.n = n
        self._count = 0  # Start at 0 for clarity

    def __iter__(self) -> Iterator[int]:
        """Returns the iterator instance."""
        return self

    def __next__(self) -> int:
        """
        Generates the next random number.

        Returns:
            int: A random number between `left` and `right` (inclusive).

        Raises:
            StopIteration: When `n` numbers have been generated.
        """
        if self._count >= self.n:
            raise StopIteration

        self._count += 1
        return random.randint(self.left, self.right)
