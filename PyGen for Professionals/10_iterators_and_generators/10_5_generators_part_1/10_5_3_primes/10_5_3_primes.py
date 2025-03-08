'''
TODO:
    Implement a generator function primes() that takes two arguments in the
    following order:
        - left — a natural number
        - right — a natural number

    The function should return a generator that produces a sequence of prime
    numbers from left to right inclusive, and then raises a StopIteration
    exception.

NOTE:
    It is guaranteed that left <= right.

    A prime number is a natural number that has exactly two distinct natural
    divisors — one and itself. One is not a prime number.
'''
from typing import Generator


def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    A prime number is a natural number greater than 1
    that has no divisors other than 1 and itself.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False

    # Check divisibility up to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def primes(left: int, right: int) -> Generator[int, None, None]:
    """
    Generate a sequence of prime numbers between 'left' and
    'right' (inclusive).

    Args:
        left (int): The starting number of the range.
        right (int): The ending number of the range.

    Yields:
        int: A prime number within the specified range.
    """
    for i in range(left, right + 1):
        if is_prime(i):
            yield i


# Example of using the generator
generator = primes(10, 30)

# Print prime numbers between 10 and 30
print(*generator)  # Output: 11 13 17 19 23 29
