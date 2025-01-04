'''
TODO:
    Write a program to check the symmetry of a square matrix with respect
    to the secondary diagonal.
'''
from typing import List


def list_convert_to_int_in_place(columns: int, row: List[str]) -> List[int]:
    """
    Converts all elements of a row to integers in place.

    Args:
        columns (int): Number of columns in the matrix (not used in this
                        function, but it defines the length of row).
        row (List[str]): A list of string values (row from the matrix).

    Returns:
        List[int]: The row with all elements converted to integers.
    """
    for cur_column in range(columns):
        row[cur_column] = int(row[cur_column])  # type: ignore
    return row  # type: ignore


def get_int_row(columns: int) -> List[int]:
    """
    Reads a row of integers from input and returns it as a list of integers.

    Args:
        columns (int): Number of columns in the matrix (used to define
                        the length of the row).

    Returns:
        List[int]: The row converted to a list of integers.
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
        List[List[int]]: The matrix as a list of lists of integers.
    """
    new_matrix = []
    for _ in range(rows):
        row = get_int_row(columns)
        new_matrix.append(row)
    return new_matrix


def check_symmetry(matrix: List[List[int]]) -> str:
    """
    Checks whether a square matrix is symmetric with respect to the
    secondary diagonal.

    Args:
        matrix (List[List[int]]): The square matrix to check for symmetry.

    Returns:
        str: "YES" if the matrix is symmetric with respect to the secondary
             diagonal, otherwise "NO".
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
                return "NO"
    return "YES"


def main() -> None:
    """
    Main function to read the input and check the symmetry of a square matrix
    with respect to the secondary diagonal.
    """
    n = int(input())
    matrix = get_matrix(n, n)
    result = check_symmetry(matrix)
    print(result)


if __name__ == "__main__":
    main()
