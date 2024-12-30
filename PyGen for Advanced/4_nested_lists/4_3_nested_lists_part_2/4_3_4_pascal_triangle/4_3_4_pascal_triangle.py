'''
TODO:
    The program is given a natural number n as input.

    Write a program that outputs the first n rows of Pascal's triangle.
'''
from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """
    Generates the first n rows of Pascal's Triangle.

    Pascal's Triangle is a triangular array where:
    - Each number is the sum of the two numbers directly above it.
    - The first and last elements of each row are 1.

    Args:
        n (int): The number of rows to generate (starting from row 1).

    Returns:
        List[List[int]]: A list of lists, where each inner list is a row
                         of Pascal's Triangle.
    """
    triangle: List = []

    for i in range(n):
        row = [1] * (i + 1)  # Start with a row filled with 1s

        # Update the elements inside the row (if they are not on the boundary)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle


# Input and output
n = int(input())  # Read the number of rows
result = pascal_triangle(n)

# Print the first n rows of Pascal's Triangle
for row in result:
    print(*row)
