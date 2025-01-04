"""
TODO:
    Two natural numbers n and m are given as input to the program.

    Write a program that creates a matrix of size n*m, filling it according
    to the pattern.

        n = 5
        m = 4

        1 2 3 4
        2 3 4 1
        3 4 1 2
        4 1 2 3
        1 2 3 4
"""
from typing import List, Tuple


def get_matrix_size() -> Tuple[int, int]:
    """
    Reads the size of the matrix from user input.

    Returns:
        tuple: (n, m), where n is the number of rows, and m is the number
                of columns.
    """
    matrix_size = input().split()
    rows = int(matrix_size[0])
    columns = int(matrix_size[1])

    return rows, columns


def get_matrix(rows_num: int, columns_num: int) -> List[List[int]]:
    """
    Generates the matrix by filling it with values according
    to the given pattern.

    Args:
        rows_num (int): The number of rows.
        columns_num (int): The number of columns.

    Returns:
        list: A 2D list representing the matrix.
    """
    matrix: List[List[int]] = []

    # Generate the first row
    first_row = list(range(1, columns_num + 1))
    matrix.append(first_row)

    for i in range(1, rows_num):
        # Shift the first row to generate the new row
        new_row = first_row[i % columns_num:] + first_row[:i % columns_num]
        matrix.append(new_row)

    return matrix


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Prints the matrix row by row.

    Args:
        matrix (List[List[int]]): The matrix to print.
    """
    for row in matrix:
        print(*row)


# Main logic
n, m = get_matrix_size()
matrix = get_matrix(n, m)
print_matrix(matrix)
