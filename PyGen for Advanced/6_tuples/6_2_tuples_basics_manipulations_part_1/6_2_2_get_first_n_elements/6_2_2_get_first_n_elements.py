'''
TODO:
    Using slices, complete the code below so that it prints the first
    6 elements of the primes tuple.

NOTE:
    The output should be the string (2, 3, 5, 7, 11, 13).
'''
from typing import Tuple


def get_first_n_elements(tup: Tuple[int, ...], n: int) -> Tuple[int, ...]:
    """
    Returns the first 'n' elements of the given tuple.

    Args:
    tup (Tuple[int, ...]): A tuple of integers.
    n (int): The number of elements to return from the beginning of the tuple.

    Returns:
    Tuple[int, ...]: A tuple containing the first 'n' elements from the
                     input tuple.
    """
    return tup[:n]


# Tuple containing prime numbers
primes: Tuple[int, ...] = (
    2, 3, 5, 7, 11,
    13, 17, 19, 23, 29,
    31, 37, 41, 43, 47,
    53, 59, 61, 67, 71
)

# Get the first 6 elements of the primes tuple
first_six_primes = get_first_n_elements(primes, 6)

# Print the result
print(first_six_primes)
