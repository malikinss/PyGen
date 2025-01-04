'''
TODO:
    Two natural numbers n and m are given as input to the program.

    Write a program that creates a matrix of size n*m and fills it with
    numbers from 1 to n⋅m according to the pattern.
        n = 3
        m = 4

        1 2 3 4
        5 6 7 8
        9 10 11 12
'''
from typing import List, Tuple


def get_matrix_size() -> Tuple[int, int]:
    """
    Reads the size of the matrix from the user input.

    Args:
        None

    Returns:
        Tuple[int, int]: A tuple containing the number of rows and columns
                         for the matrix.
    """
    matrix_size = input().split()

    rows = int(matrix_size[0])
    columns = int(matrix_size[1])

    return rows, columns


def get_next_row(previous_element: int, last_element: int) -> List[int]:
    """
    Generates the next row of the matrix with consecutive numbers.

    Args:
        previous_element (int): The last number of the previous row.
        last_element (int): The last number of the current row.

    Returns:
        List[int]: A list of consecutive integers for the row.
    """
    row = [elem for elem in range(previous_element + 1, last_element + 1)]
    return row


def get_matrix_n_X_m(n: int, m: int) -> List[List[int]]:
    """
    Creates a matrix of size n x m, filling it with consecutive numbers
    from 1 to n * m.

    Args:
        n (int): The number of rows in the matrix.
        m (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: A matrix represented as a list of lists, where
                         each inner list is a row.
    """
    matrix = []
    previous_element = 0

    for i in range(1, n + 1):
        last_element = m * i
        row = get_next_row(previous_element, last_element)
        matrix.append(row)
        previous_element = last_element

    return matrix


def print_matrix_rows(matrix: List[List[int]]) -> None:
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
matrix = get_matrix_n_X_m(n, m)
print_matrix_rows(matrix)
