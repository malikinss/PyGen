'''
TODO:
    Given a square matrix of numbers, write a program that mirrors
    its elements relative to the horizontal axis of symmetry.
'''
from typing import List


def mirror_matrix(matrix: List[List[int]], n: int) -> None:
    """
    Mirrors the matrix elements relative to the horizontal axis of symmetry.

    Args:
        matrix (List[List[int]]): The square matrix.
        n (int): The number of rows and columns of the matrix.
    """
    for i in range(n // 2):
        # Swap the rows to mirror the matrix along the horizontal axis
        matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]


def main() -> None:
    """
    Main function to read input, mirror the matrix, and print the result.
    """
    n: int = int(input())  # Number of rows/columns of the square matrix
    matrix: List = [list(map(int, input().split())) for _ in range(n)]

    mirror_matrix(matrix, n)

    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
