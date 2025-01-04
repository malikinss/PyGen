"""
TODO:
    Two natural numbers n and m are given as input to the program.

    Write a program that creates a matrix of size n*m and fills it with
    numbers from 1 to n⋅m according to the pattern.
        n = 3
        m = 4

        1 2 3 4
        5 6 7 8
        9 10 11 12
"""
from typing import List


def get_matrix_size() -> tuple[int, int]:
    """
    Reads the size of the matrix from user input.

    Args:
        None

    Returns:
        tuple[int, int]: A tuple containing the number of rows (n)
                         and columns (m) for the matrix.
    """
    n, m = map(int, input().split())
    return n, m


def get_matrix(n: int, m: int) -> List[List[int]]:
    """
    Creates an n x m matrix, filling it with numbers from 1 to n * m
    following a row-wise pattern.

    Args:
        n (int): The number of rows in the matrix.
        m (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: The filled matrix as a list of lists.
    """
    matrix = []
    current_number = 1

    for i in range(n):
        row = []
        for j in range(m):
            row.append(current_number)
            current_number += 1
        matrix.append(row)

    return matrix


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Prints each row of the matrix.

    Args:
        matrix (List[List[int]]): The matrix to be printed.

    Returns:
        None
    """
    for row in matrix:
        print(*row)


# Main logic
n, m = get_matrix_size()
matrix = get_matrix(n, m)
print_matrix(matrix)
