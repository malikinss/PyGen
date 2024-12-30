'''
TODO:
    Write a program that rotates a square matrix of numbers 90∘ clockwise.0
'''
from typing import List


def rotate_matrix_clockwise(
    matrix: List[List[int]], n: int
) -> List[List[int]]:
    """
    Rotates a square matrix 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): The original square matrix.
        n (int): The size of the matrix (number of rows/columns).

    Returns:
        List[List[int]]: The rotated matrix.
    """
    rotated_matrix = []

    for i in range(n):
        row = [matrix[n - 1 - j][i] for j in range(n)]
        rotated_matrix.append(row)

    return rotated_matrix


def main() -> None:
    """
    Main function to read input, rotate the matrix, and print the result.
    """
    n: int = int(input())  # Size of the square matrix
    matrix: List = [list(map(int, input().split())) for _ in range(n)]

    rotated_matrix = rotate_matrix_clockwise(matrix, n)

    for row in rotated_matrix:
        print(*row)


if __name__ == "__main__":
    main()
