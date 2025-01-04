'''
TODO:
    A Latin square of order n is a square matrix of size n*n, each row and
    each column of which contains all the numbers from 1 to n.

    Write a program that checks whether a given square matrix
    is a Latin square.
'''
from typing import List


def list_convert_to_int_in_place(columns: int, row: List[str]) -> List[int]:
    """
    Converts all elements of a row from strings to integers in place.

    Args:
        columns (int): Number of columns in the matrix (not used in this
                       function, but defines the length of the row).
        row (List[str]): A list of strings representing a row of the matrix.

    Returns:
        List[int]: A row with elements converted to integers.
    """
    for cur_column in range(columns):
        row[cur_column] = int(row[cur_column])  # type: ignore
    return row  # type: ignore


def get_int_row(columns: int) -> List[int]:
    """
    Reads a row from input and converts it to a list of integers.

    Args:
        columns (int): Number of columns in the matrix
                       (defines the row's length).

    Returns:
        List[int]: The row as a list of integers.
    """
    row = input().split()
    row = list_convert_to_int_in_place(columns, row)  # type: ignore
    return row  # type: ignore


def get_matrix(rows: int, columns: int) -> List[List[int]]:
    """
    Reads a matrix from input where each row is a list of integers.

    Args:
        rows (int): Number of rows in the matrix.
        columns (int): Number of columns in the matrix.

    Returns:
        List[List[int]]: The matrix as a list of rows (lists of integers).
    """
    new_matrix = []
    for _ in range(rows):
        row = get_int_row(columns)
        new_matrix.append(row)
    return new_matrix


def get_row_from_matrix(row_id: int, matrix: List[List[int]]) -> List[int]:
    """
    Retrieves a specific row from the matrix.

    Args:
        row_id (int): The row index to retrieve.
        matrix (List[List[int]]): The matrix from which to retrieve the row.

    Returns:
        List[int]: The row at the specified index.
    """
    return matrix[row_id]


def get_column_as_row_from_matrix(
    column_id: int, rows_number: int, matrix: List[List[int]]
) -> List[int]:
    """
    Retrieves a specific column from the matrix as a list.

    Args:
        column_id (int): The column index to retrieve.
        rows_number (int): The number of rows in the matrix.
        matrix (List[List[int]]): The matrix from which to retrieve the column.

    Returns:
        List[int]: The column at the specified index.
    """
    return [matrix[i][column_id] for i in range(rows_number)]


def check_row(
    row: List[int], left_border_of_sorting: int, right_border_of_sorting: int
) -> bool:
    """
    Checks if a row contains all integers from `left_border_of_sorting`
    to `right_border_of_sorting`.

    Args:
        row (List[int]): The row to check.
        left_border_of_sorting (int): The start value of the range.
        right_border_of_sorting (int): The end value of the range.

    Returns:
        bool: True if the row contains all integers
              from `left_border_of_sorting` to `right_border_of_sorting`,
              False otherwise.
    """
    sorted_row = sorted(row)
    for i in range(left_border_of_sorting, right_border_of_sorting + 1):
        if i != sorted_row[i - 1]:
            return False
    return True


def check_all_rows(rows_number: int, matrix: List[List[int]]) -> bool:
    """
    Checks if all rows in the matrix are valid for a Latin square.

    Args:
        rows_number (int): The number of rows in the matrix.
        matrix (List[List[int]]): The matrix to check.

    Returns:
        bool: True if all rows are valid, False otherwise.
    """
    for i in range(rows_number):
        row = get_row_from_matrix(i, matrix)
        if not check_row(row, 1, rows_number):
            return False
    return True


def check_all_columns(columns_number: int, matrix: List[List[int]]) -> bool:
    """
    Checks if all columns in the matrix are valid for a Latin square.

    Args:
        columns_number (int): The number of columns in the matrix.
        matrix (List[List[int]]): The matrix to check.

    Returns:
        bool: True if all columns are valid, False otherwise.
    """
    for i in range(columns_number):
        column = get_column_as_row_from_matrix(i, columns_number, matrix)
        if not check_row(column, 1, columns_number):
            return False
    return True


def check_latin_square(matrix: List[List[int]], size: int) -> bool:
    """
    Checks whether the given matrix is a Latin square.

    Args:
        matrix (List[List[int]]): The matrix to check.
        size (int): The size of the matrix (both rows and columns).

    Returns:
        bool: True if the matrix is a Latin square, False otherwise.
    """
    return check_all_rows(size, matrix) and check_all_columns(size, matrix)


def main() -> None:
    """
    Main function to read input, check if the matrix is a Latin square,
    and print the result.
    """
    n = int(input())
    matrix = get_matrix(n, n)

    if check_latin_square(matrix, n):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
