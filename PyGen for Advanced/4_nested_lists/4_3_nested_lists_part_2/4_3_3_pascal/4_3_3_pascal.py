'''
TODO:
    Pascal's triangle is an infinite table of binomial coefficients that has
    a triangular shape.

    This triangle has ones at the top and on the sides.

    Each number is equal to the sum of the two numbers above it.
        0:     1
        1:    1 1
        2:   1 2 1
        3:  1 3 3 1
        4: 1 4 6 4 1
        .....

    The input to the program is the number n.

    Write a program that returns the specified row of Pascal's triangle
    as a list (rows are numbered starting from zero).

NOTE:
    The solution can be conveniently written as a function pascal(),
    which takes a row number and returns the corresponding row of Pascal's
    triangle.
'''
from typing import List


def pascal(n: int) -> List[int]:
    """
    Returns the nth row of Pascal's Triangle.

    Pascal's Triangle is a triangular array of binomial coefficients, where:
        - The first and last elements of each row are 1.
        - Each element is the sum of the two elements directly above it.

    Args:
        n (int): The row number (starting from 0) of Pascal's Triangle
                 to return.

    Returns:
        List[int]: The nth row of Pascal's Triangle.
    """
    row = [1]
    for i in range(n):
        for j in range(len(row) - 1):
            row[j] = row[j] + row[j + 1]
        row.insert(0, 1)

    return row


# Example usage:
n = int(input())
print(pascal(n))
