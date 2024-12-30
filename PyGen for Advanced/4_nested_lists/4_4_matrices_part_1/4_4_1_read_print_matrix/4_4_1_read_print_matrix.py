'''
TODO:
    The program is given two natural numbers n and m as input, each
    on a separate line - the number of rows and columns in the matrix.

    Then the matrix elements themselves are entered - words, each on
    a separate line; the elements of the first row come in a row,
    then the second, and so on.

    Write a program that first reads the matrix elements one by one,
    then outputs them as a matrix.
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

    for i in range(n):
        row: List[str] = []
        for j in range(m):
            element: str = input()  # Read matrix element
            row.append(element)
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


# Input for matrix dimensions
n: int = int(input())
m: int = int(input())

# Read and print the matrix
matrix = read_matrix(n, m)
print_matrix(matrix)
