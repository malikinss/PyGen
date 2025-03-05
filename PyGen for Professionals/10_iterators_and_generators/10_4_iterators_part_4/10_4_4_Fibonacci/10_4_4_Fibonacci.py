'''
TODO:
    Implement a Fibonacci class that produces iterators whose constructor
    takes no arguments.

    The iterator of class Fibonacci must generate an infinite sequence
    of Fibonacci numbers, starting with 1.

NOTE:
    The Fibonacci sequence is a sequence of natural numbers, where each
    successive number is the sum of the two preceding ones:
        1,1,2,3,5,8,13,21,34
'''


class Fibonacci:
    """
    An iterator that generates an infinite sequence of Fibonacci numbers.

    Methods:
        __iter__() -> Fibonacci: Returns the iterator itself.
        __next__() -> int: Returns the next Fibonacci number.

    Example:
        fib = Fibonacci()
        for _ in range(5):
            print(next(fib))  # Output: 1, 1, 2, 3, 5
    """

    def __init__(self) -> None:
        self.prev: int = 0
        self.cur: int = 1

    def __iter__(self) -> "Fibonacci":
        return self

    def __next__(self) -> int:
        # Return the current Fibonacci number
        fib = self.cur

        # Update the previous and current numbers for the next call
        self.prev, self.cur = self.cur, self.prev + self.cur

        return fib
