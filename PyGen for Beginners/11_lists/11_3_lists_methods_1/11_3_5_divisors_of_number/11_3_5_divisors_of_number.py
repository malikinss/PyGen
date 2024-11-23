'''
TODO:
    The input to the program is a natural number n.

    Write a program that creates a list of divisors of a given number.
'''
from typing import List


def divisors_of_number(n: int) -> List[int]:
    """
    This function takes a number n and returns a list of divisors
    of the given number.

    Args:
    n (int): The number for which divisors are to be found.

    Returns:
    List[int]: A list of divisors of n.
    """
    return [i for i in range(1, n+1) if n % i == 0]


# Input: The number n
n = int(input())

# Call the function and print the result
result = divisors_of_number(n)
print(result)
