'''
TODO:
    Write a program that raises a square matrix to the m-th power.
'''
from typing import List
from copy import deepcopy


def get_matrix_size() -> int:
    """
    Reads the size of a square matrix from input.

    Returns:
        int: Number of rows and columns (for square matrix).
    """
    return int(input("Enter matrix size: "))


def read_matrix_row(columns: int) -> List[int]:
    """
    Reads a single row of matrix and converts to integers.

    Args:
        columns (int): Number of columns.

    Returns:
        List[int]: List of integers representing the row.
    """
    return list(map(int, input("Enter matrix row: ").split()))


def get_matrix(size: int) -> List[List[int]]:
    """
    Reads a square matrix from input.

    Args:
        size (int): Size of the matrix (number of rows and columns).

    Returns:
        List[List[int]]: 2D list representing the matrix.
    """
    return [read_matrix_row(size) for _ in range(size)]


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Prints a matrix row by row.

    Args:
        matrix (List[List[int]]): 2D list representing the matrix.
    """
    for row in matrix:
        print(*row)


def matrix_multiplication(matrix1: List[List[int]],
                          matrix2: List[List[int]],
                          size: int) -> List[List[int]]:
    """
    Multiplies two square matrices.

    Args:
        matrix1 (List[List[int]]): First matrix.
        matrix2 (List[List[int]]): Second matrix.
        size (int): Size of the matrices.

    Returns:
        List[List[int]]: Result of matrix multiplication.
    """
    result = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            result[i][j] = sum(
                matrix1[i][k] * matrix2[k][j] for k in range(size)
            )

    return result


def matrix_power(
    matrix: List[List[int]], degree: int, size: int
) -> List[List[int]]:
    """
    Raises a square matrix to the power of 'degree'.

    Args:
        matrix (List[List[int]]): Matrix to raise to power.
        degree (int): Power to raise the matrix to.
        size (int): Size of the matrix.

    Returns:
        List[List[int]]: Matrix raised to the specified power.
    """
    result = deepcopy(matrix)

    while degree > 1:
        if degree % 2 == 1:
            result = matrix_multiplication(result, matrix, size)
        matrix = matrix_multiplication(matrix, matrix, size)
        degree //= 2

    return result


def main() -> None:
    """
    Main function to read matrix, raise to power, and print result.
    """
    # Step 1: Read matrix size and initialize the matrix
    size = get_matrix_size()
    matrix = get_matrix(size)

    # Step 2: Read the exponent for matrix power
    degree = int(input("Enter matrix power: "))

    # Step 3: Calculate the power of the matrix
    result = matrix_power(matrix, degree, size)

    # Step 4: Print the result
    print("Resulting matrix:")
    print_matrix(result)


if __name__ == "__main__":
    main()
