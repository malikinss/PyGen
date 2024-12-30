'''
TODO:
    Write a program that prints the maximum element to the left of the main
    diagonal of a square matrix.

NOTE:
    The elements of the main diagonal are also taken into account.
'''
from typing import List


def read_square_matrix(n: int) -> List[List[int]]:
    """
    Reads an n x n square matrix from user input.

    Args:
        n (int): Size of the square matrix.

    Returns:
        List[List[int]]: Square matrix as a list of lists of integers.
    """
    return [list(map(int, input().split())) for _ in range(n)]


def find_max_left_diagonal(matrix: List[List[int]]) -> int:
    """
    Finds the maximum element to the left of the main diagonal
    (including the diagonal).

    Args:
        matrix (List[List[int]]): Square matrix.

    Returns:
        int: Maximum element to the left of the main diagonal.
    """
    maximum = matrix[0][0]  # Initialize with the top-left element
    n = len(matrix)

    for i in range(n):
        # Include elements from the main diagonal and to the left
        for j in range(i + 1):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

    return maximum


def main() -> None:
    """
    Main function to read input, compute the maximum, and print the result.
    """
    n: int = int(input())
    matrix = read_square_matrix(n)

    print(find_max_left_diagonal(matrix))


if __name__ == "__main__":
    main()
