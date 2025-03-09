'''
TODO:
    Implement a generator function palindromes() that takes no arguments.

    The function should return a generator that produces an infinite sequence
    of palindromic natural numbers.

NOTE:
    A palindrome number is a number that reads the same from right to left
    as it does from left to right.
'''
from typing import Generator


def palindromes() -> Generator[int, None, None]:
    """
    Generates an infinite sequence of palindromic natural numbers.

    A palindrome number is a number that reads the same from right to left as
    it does from left to right.

    Yields:
        int: Each palindromic number in the sequence.

    Example:
        for num in palindromes():
            if num > 100:
                break
            print(num)
        # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, ...
    """

    def is_palindrome_number(n: int) -> bool:
        """
        Check if a given number is a palindrome.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is a palindrome, False otherwise.
        """
        # Convert the number to a string and compare it to its reverse
        return str(n) == str(n)[::-1]

    def generate_palindrome() -> Generator[int, None, None]:
        """
        Infinite generator that yields palindromic numbers.

        Yields:
            int: Each palindromic number in the sequence.
        """
        num = 1
        while True:
            if is_palindrome_number(num):
                yield num
            num += 1

    yield from generate_palindrome()
