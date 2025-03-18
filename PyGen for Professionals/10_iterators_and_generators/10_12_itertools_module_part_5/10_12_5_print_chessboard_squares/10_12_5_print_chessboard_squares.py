'''
TODO:
    You have access to a program that prints all the squares of a chessboard
    in alphabetical order, separated by spaces.

    Rewrite this program using the product() function to do the same thing.

NOTE:
    The initial part of the answer looks like this:
        a1 a2 a3 a4 a5 a6 a7 a8 b1 b2 ...
'''
from string import ascii_lowercase
from itertools import product
from typing import List


def print_chessboard_squares() -> None:
    """
    Prints all squares of a chessboard in alphabetical order
    (e.g., a1, a2, ..., h8), using the product() function to generate all
    combinations of letters and digits.
    """
    letters = ascii_lowercase[:8]
    digits = [1, 2, 3, 4, 5, 6, 7, 8]

    result: List[tuple] = product(letters, digits)

    for cell in result:
        print(*cell, sep='', end=' ')


print_chessboard_squares()
