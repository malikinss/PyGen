'''
TODO:
    The input to the program is a natural number n.

    Write a list expression program that generates a list containing
    the squares of numbers from 1 to n (inclusive), and then prints its
    elements line by line, that is, each on a separate line.
'''
from typing import List


def generate_squares(n: int) -> List[int]:
    """
    Generates a list of squares of numbers from 1 to n (inclusive).

    Args:
        n (int): The upper limit of the range.

    Returns:
        List[int]: A list of squares of numbers from 1 to n.
    """
    return [i**2 for i in range(1, n+1)]


def print_squares() -> None:
    """
    Prompts the user for a number and prints the squares of numbers from 1 to
    that number (inclusive),
    each on a new line.
    """
    n = int(input("Enter a natural number: "))
    squares = generate_squares(n)
    print(*squares, sep='\n')


# Calling the function to print squares
print_squares()
