'''
TODO:
    Implement a Square class that produces iterators whose constructor takes
    one argument:
        - n is a natural number,

    The iterator of the Square class should generate a sequence of n numbers,
    each of which is the square of the next natural number, and then raise
    a StopIteration exception.

NOTE:
The sequence of squares of natural numbers begins with the square of 1.
'''
from typing import Iterator


class Square:
    """
    An iterator that generates the first `n` squares of natural numbers.

    Args:
        n (int): The number of squares to generate.

    Methods:
        __iter__() -> Iterator[int]: Returns the iterator itself.
        __next__() -> int: Returns the next square of a natural number, then
        raises StopIteration when `n` values are generated.

    Example:
        squares = Square(5)
        print(list(squares))  # Output: [1, 4, 9, 16, 25]
    """

    def __init__(self, n: int) -> None:
        self.n: int = n
        self.num: int = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.num >= self.n:
            raise StopIteration
        self.num += 1
        return self.num ** 2
