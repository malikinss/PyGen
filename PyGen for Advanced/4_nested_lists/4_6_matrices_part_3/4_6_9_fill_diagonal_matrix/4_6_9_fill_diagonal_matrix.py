"""
TODO:
    Two natural numbers n and m are given as input to the program.

    Write a program that creates an n*m matrix, filling it with "diagonals"
    according to the pattern.

        n = 3
        m = 5

        1  2  4  7  10
        3  5  8  11 13
        6  9  12 14 15
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


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Prints the matrix row by row.

    Args:
        matrix (List[List[int]]): The matrix to print.
    """
    for row in matrix:
        print(*row)


def get_empty_matrix(
    number_of_rows: int, number_of_columns: int
) -> List[List[int]]:
    """
    Creates an empty matrix of size n*m, filled with zeros.

    Args:
        number_of_rows (int): The number of rows in the matrix.
        number_of_columns (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: An n*m matrix filled with zeros.
    """
    matrix = []

    for _ in range(number_of_rows):
        row = [0] * number_of_columns
        matrix.append(row)

    return matrix


def fill_diagonal_matrix(
    matrix: List[List[int]], number_of_rows: int, number_of_columns: int
) -> List[List[int]]:
    """
    Fills the matrix with values in a diagonal pattern.

    Args:
        matrix (List[List[int]]): The matrix to fill.
        number_of_rows (int): The number of rows in the matrix.
        number_of_columns (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: The matrix filled with values in the diagonal pattern.
    """
    current_element = 1

    for sum_of_indexes in range(number_of_rows + number_of_columns - 1):
        for row in range(number_of_rows):
            for column in range(number_of_columns):
                if row + column == sum_of_indexes:
                    matrix[row][column] = current_element
                    current_element += 1

    return matrix


def get_matrix(number_of_rows: int, number_of_columns: int) -> List[List[int]]:
    """
    Generates the matrix and fills it with the diagonal pattern.

    Args:
        number_of_rows (int): The number of rows in the matrix.
        number_of_columns (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: The matrix filled with diagonal values.
    """
    matrix = get_empty_matrix(number_of_rows, number_of_columns)
    matrix = fill_diagonal_matrix(matrix, number_of_rows, number_of_columns)

    return matrix


# Main logic
n, m = get_matrix_size()
matrix = get_matrix(n, m)
print_matrix(matrix)
