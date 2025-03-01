'''
TODO:
    The Tribonacci sequence is a sequence of natural numbers where each
    subsequent number is the sum of the three previous ones:
        1, 1, 1, 3, 5, 9, 17, 31, 57, 105 …

    Implement the tribonacci() function using recursion and memoization that
    takes one argument:
        n - is a natural number

    The function should return the n-th term of the Tribonacci sequence.
'''
from typing import Dict


def tribonacci(n: int) -> int:
    """
    Computes the n-th term of the Tribonacci sequence.

    Args:
        n (int): The position in the Tribonacci sequence (1-based index).

    Returns:
        int: The n-th term of the Tribonacci sequence.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    # Memoization dictionary to store computed Tribonacci numbers
    memo: Dict[int, int] = {1: 1, 2: 1, 3: 1}

    def _tribonacci_recursive(n: int) -> int:
        """
        Recursive helper function for computing Tribonacci numbers with
        memoization.

        Args:
            n (int): The position in the Tribonacci sequence (1-based index).

        Returns:
            int: The n-th term of the Tribonacci sequence.
        """
        if n not in memo:
            memo[n] = (
                _tribonacci_recursive(n - 3)
                + _tribonacci_recursive(n - 2)
                + _tribonacci_recursive(n - 1)
            )

    return _tribonacci_recursive(n)


# Test cases
print(tribonacci(1))  # Output: 1
print(tribonacci(7))  # Output: 17
print(tribonacci(4))  # Output: 3
