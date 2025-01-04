"""
TODO:
    The program input is a natural number n.

    Write a program that creates an n*n matrix, filling it according
    to the pattern.
        n = 5

        1 1 1 1 1
        0 1 1 1 0
        0 0 1 0 0
        0 1 1 1 0
        1 1 1 1 1
"""
from typing import List


def get_matrix_size() -> int:
    """
    Reads the size of the matrix from user input.

    Args:
        None

    Returns:
        int: The size (n) of the matrix.
    """
    return int(input())


def get_row(row_idx: int, size: int) -> List[int]:
    """
    Generates a row for the matrix based on the current row index.

    Args:
        row_idx (int): The index of the current row.
        size (int): The size of the matrix (n).

    Returns:
        List[int]: A list representing the row, filled with 1s and 0s.
    """
    row = [0] * size  # Start with all 0s

    # Set 1s in the middle section
    start = min(row_idx, size - 1 - row_idx)  # The outer boundary of the 1s
    end = size - start  # The end boundary of the 1s

    for i in range(start, end):
        row[i] = 1
    return row


def get_matrix(size: int) -> List[List[int]]:
    """
    Generates an n x n matrix based on the given size (n).

    Args:
        size (int): The size of the matrix (n).

    Returns:
        List[List[int]]: The matrix as a list of lists.
    """
    matrix = []
    for row_idx in range(size):
        matrix.append(get_row(row_idx, size))
    return matrix


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Prints the matrix row by row.

    Args:
        matrix (List[List[int]]): The matrix to print.

    Returns:
        None
    """
    for row in matrix:
        print(*row)


# Main logic
size = get_matrix_size()
matrix = get_matrix(size)
print_matrix(matrix)
