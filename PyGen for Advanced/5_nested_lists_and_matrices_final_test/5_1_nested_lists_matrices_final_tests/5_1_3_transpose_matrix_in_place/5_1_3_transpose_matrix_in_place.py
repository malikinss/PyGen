'''
TODO:
    Write a program that transposes a square matrix.

NOTE:
    A transposed matrix is a matrix obtained from the original matrix
    by replacing rows with columns.

    The problem can be solved without using an auxiliary list.
'''
from typing import List


def get_square_matrix(n: int) -> List[List[int]]:
    """
    Reads a square matrix of size n from user input.

    Args:
        n (int): Size of the matrix (n x n).

    Returns:
        List[List[int]]: The square matrix of integers.
    """
    return [[int(i) for i in input().split()] for _ in range(n)]


def transpose_matrix_in_place(matrix: List[List[int]], n: int) -> None:
    """
    Transposes a square matrix in place by swapping rows and columns.

    Args:
        matrix (List[List[int]]): The square matrix to transpose.
        n (int): Size of the matrix (n x n).

    Returns:
        None: The matrix is transposed in place.
    """
    for i in range(n):
        for j in range(i + 1, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


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


def main() -> None:
    """
    Main function to handle matrix input, transpose, and output.
    """
    # Read matrix size
    n = int(input("Enter the size of the square matrix: "))

    # Get matrix from user input
    matrix = get_square_matrix(n)

    # Transpose the matrix in place
    transpose_matrix_in_place(matrix, n)

    # Print the transposed matrix
    print_matrix(matrix)


if __name__ == "__main__":
    main()
