'''
TODO:
    Write a program that checks the symmetry of a square matrix about
    the main diagonal.
'''
from typing import List


def check_symmetry(matrix: List[List[int]], n: int) -> str:
    """
    Checks if a square matrix is symmetric about its main diagonal.

    Args:
        matrix (List[List[int]]): The square matrix.
        n (int): The number of rows and columns of the matrix.

    Returns:
        str: 'YES' if the matrix is symmetric, 'NO' otherwise.
    """
    for i in range(n):
        for j in range(i, n):  # Only check the upper triangle of the matrix
            if matrix[i][j] != matrix[j][i]:
                return "NO"
    return "YES"


def main() -> None:
    """
    Main function to read input, check the matrix symmetry, and print
    the result.
    """
    n: int = int(input())  # Number of rows/columns of the square matrix
    matrix: List[List[int]] = [
        list(map(int, input().split())) for _ in range(n)
    ]

    result = check_symmetry(matrix, n)
    print(result)


if __name__ == "__main__":
    main()
