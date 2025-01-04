"""
TODO:
    Two natural numbers n and m are given as input to the program.

    Write a program that creates a matrix of size n*m, filling it with
    a “snake” according to the pattern.

        n = 3
        m = 5

        1  2  3  4  5
        10 9  8  7  6
        11 12 13 14 15
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


def get_row_even(
    row: List[int], final_element: int, first_element: int
) -> List[int]:
    """
    Fills the row with elements in decreasing order.

    Args:
        row (List[int]): The row to be filled.
        final_element (int): The last element to be added in the row.
        first_element (int): The first element to be added in the row.

    Returns:
        List[int]: The filled row with elements in decreasing order.
    """
    for element in range(final_element, first_element - 1, -1):
        row.append(element)
    return row


def get_row_odd(
    row: List[int], final_element: int, first_element: int
) -> List[int]:
    """
    Fills the row with elements in increasing order.

    Args:
        row (List[int]): The row to be filled.
        final_element (int): The last element to be added in the row.
        first_element (int): The first element to be added in the row.

    Returns:
        List[int]: The filled row with elements in increasing order.
    """
    for element in range(first_element, final_element + 1):
        row.append(element)

    return row


def get_row(current_row_number: int, number_of_columns: int) -> List[int]:
    """
    Generates the row based on the current row number and the number
    of columns.

    Args:
        current_row_number (int): The row number (1-indexed).
        number_of_columns (int): The number of columns in the matrix.

    Returns:
        List[int]: The generated row according to the snake pattern.
    """
    row: List = []

    final_element = current_row_number * number_of_columns
    first_element = final_element - number_of_columns + 1

    if current_row_number % 2 == 0:
        row = get_row_even(row, final_element, first_element)
    else:
        row = get_row_odd(row, final_element, first_element)

    return row


def get_matrix(number_of_rows: int, number_of_columns: int) -> List[List[int]]:
    """
    Generates the matrix with the snake pattern based on the number of rows
    and columns.

    Args:
        number_of_rows (int): The number of rows in the matrix.
        number_of_columns (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: The matrix generated with the snake pattern.
    """
    matrix = []

    for current_row_number in range(1, number_of_rows + 1):
        row = get_row(current_row_number, number_of_columns)
        matrix.append(row)

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
