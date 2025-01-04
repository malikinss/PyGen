'''
TODO:
    An odd natural number n is fed to the input of the program.

    Write a program that creates a matrix of size n*n by filling it with
    the symbols "." .

    Then fill the middle row and column of the matrix, the main and secondary
    diagonals of the matrix with the symbols *.

    Output the resulting matrix to the screen, separating the elements
    with spaces.
'''
from typing import List


def print_matrix(matrix: List[List[str]], rows: int) -> None:
    """
    Prints the matrix row by row.

    Args:
        matrix (List[List[str]]): The matrix to be printed.
        rows (int): The number of rows in the matrix.

    Returns:
        None
    """
    for i in range(rows):
        print(*matrix[i])


def get_matrix_of_points(size: int) -> List[List[str]]:
    """
    Creates a matrix of size n x n filled with the symbol '.'.

    Args:
        size (int): The size of the matrix.

    Returns:
        List[List[str]]: A matrix filled with dots.
    """
    return [["." for _ in range(size)] for _ in range(size)]


def fill_middle_column(
    columns_number: int, rows_number: int, matrix: List[List[str]]
) -> List[List[str]]:
    """
    Fills the middle column of the matrix with the symbol '*'.

    Args:
        columns_number (int): Number of columns.
        rows_number (int): Number of rows.
        matrix (List[List[str]]): The matrix to be modified.

    Returns:
        List[List[str]]: The updated matrix with the middle column filled.
    """
    middle_column_id = columns_number // 2
    for i in range(rows_number):
        matrix[i][middle_column_id] = '*'
    return matrix


def fill_middle_row(
    columns_number: int, rows_number: int, matrix: List[List[str]]
) -> List[List[str]]:
    """
    Fills the middle row of the matrix with the symbol '*'.

    Args:
        columns_number (int): Number of columns.
        rows_number (int): Number of rows.
        matrix (List[List[str]]): The matrix to be modified.

    Returns:
        List[List[str]]: The updated matrix with the middle row filled.
    """
    middle_row_id = rows_number // 2
    for j in range(columns_number):
        matrix[middle_row_id][j] = '*'
    return matrix


def fill_main_diagonal(size: int, matrix: List[List[str]]) -> List[List[str]]:
    """
    Fills the main diagonal of the matrix with the symbol '*'.

    Args:
        size (int): Size of the matrix.
        matrix (List[List[str]]): The matrix to be modified.

    Returns:
        List[List[str]]: The updated matrix with the main diagonal filled.
    """
    for i in range(size):
        matrix[i][i] = '*'
    return matrix


def fill_secondary_diagonal(
    size: int, matrix: List[List[str]]
) -> List[List[str]]:
    """
    Fills the secondary diagonal of the matrix with the symbol '*'.

    Args:
        size (int): Size of the matrix.
        matrix (List[List[str]]): The matrix to be modified.

    Returns:
        List[List[str]]: The updated matrix with the secondary diagonal filled.
    """
    for i in range(size):
        matrix[i][size - i - 1] = '*'
    return matrix


def fill_snowflake_in_matrix(
    size: int, matrix: List[List[str]]
) -> List[List[str]]:
    """
    Fills the matrix with a snowflake pattern by filling the main and
    secondary diagonals, the middle row, and the middle column with '*'.

    Args:
        size (int): Size of the matrix.
        matrix (List[List[str]]): The matrix to be modified.

    Returns:
        List[List[str]]: The updated matrix with the snowflake pattern.
    """
    matrix = fill_middle_column(size, size, matrix)
    matrix = fill_middle_row(size, size, matrix)
    matrix = fill_main_diagonal(size, matrix)
    matrix = fill_secondary_diagonal(size, matrix)
    return matrix


def main() -> None:
    """
    Main function of the program. Prompts the user for the size of the matrix
    and prints the resulting snowflake pattern.
    """
    n = int(input("Enter an odd natural number: "))
    if n % 2 == 0:
        print('Input number should be odd')
    else:
        matrix = get_matrix_of_points(n)
        matrix = fill_snowflake_in_matrix(n, matrix)
        print_matrix(matrix, n)


if __name__ == "__main__":
    main()
