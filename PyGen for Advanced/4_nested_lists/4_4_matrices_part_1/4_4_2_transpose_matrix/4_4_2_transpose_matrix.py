'''
TODO:
    The program is given two natural numbers n and m as input,
    each on a separate line — the number of rows and columns in the matrix.

    Then the matrix elements themselves are entered — words,
    each on a separate line; the elements of the first row come in a row,
    then the second, and so on.

    Write a program that reads the matrix elements one by one, outputs them
    as a matrix, outputs an empty row, and then the same matrix again,
    but with the rows and columns swapped: the first row is output
    as the first column, and so on.
'''
from typing import List


def read_matrix(n: int, m: int) -> List[List[str]]:
    """
    Reads a matrix of size n x m from user input, where each element
    is provided line by line.

    Args:
        n (int): Number of rows in the matrix.
        m (int): Number of columns in the matrix.

    Returns:
        List[List[str]]: A matrix represented as a list of lists of strings.
    """
    matrix: List[List[str]] = []
    for _ in range(n):
        row: List[str] = [input() for _ in range(m)]
        matrix.append(row)
    return matrix


def print_matrix(matrix: List[List[str]]) -> None:
    """
    Prints the matrix row by row.

    Args:
        matrix (List[List[str]]): The matrix to be printed.
    """
    for row in matrix:
        print(*row)


def transpose_matrix(matrix: List[List[str]]) -> List[List[str]]:
    """
    Transposes the given matrix (swaps rows and columns).

    Args:
        matrix (List[List[str]]): The matrix to transpose.

    Returns:
        List[List[str]]: The transposed matrix.
    """
    n = len(matrix)
    m = len(matrix[0]) if matrix else 0
    return [[matrix[row][col] for row in range(n)] for col in range(m)]


# Input for matrix dimensions
n: int = int(input())
m: int = int(input())

# Read and print the matrix
matrix = read_matrix(n, m)
print_matrix(matrix)

# Print an empty line
print()

# Transpose and print the matrix
transposed = transpose_matrix(matrix)
print_matrix(transposed)
