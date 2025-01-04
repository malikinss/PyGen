'''
TODO:
    The program input is a natural number n.

    Write a program that creates an n*n matrix and fills it according
    to the following rule:
        - the numbers on the side diagonal are equal to 1;
        - numbers above this diagonal are equal to 0;
        - the numbers below this diagonal are equal to 2.

    Display the resulting matrix on the screen.

    Separate numbers in a line with one space.
'''
from typing import List


def get_matrix_size() -> int:
    """Get the size of the matrix."""
    return int(input())


def print_matrix(matrix: List[List[int]]) -> None:
    """Print the matrix row by row."""
    for row in matrix:
        print(*row)


def create_matrix_with_side_diagonal(n: int) -> List[List[int]]:
    """Create the matrix with the side diagonal pattern."""
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if j < (n - i - 1):
                row.append(0)
            elif j > (n - i - 1):
                row.append(2)
            else:
                row.append(1)
        matrix.append(row)
    return matrix


# Main logic
n: int = get_matrix_size()
matrix: List[List[int]] = create_matrix_with_side_diagonal(n)
print_matrix(matrix)
