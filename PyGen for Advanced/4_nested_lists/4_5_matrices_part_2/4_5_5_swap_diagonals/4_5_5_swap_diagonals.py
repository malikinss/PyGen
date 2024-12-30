'''
TODO:
    Given a square matrix of numbers, write a program that swaps the elements
    on the main and secondary diagonals, while each element must remain
    in the same column (that is, in each column, you need to swap the element
    on the main diagonal and on the secondary diagonal).
'''
from typing import List


def swap_diagonals(matrix: List[List[int]], n: int) -> None:
    """
    Swaps the elements on the main and secondary diagonals of a square matrix.

    Args:
        matrix (List[List[int]]): The square matrix.
        n (int): The number of rows and columns of the matrix.
    """
    for i in range(n):
        # Swap elements on the main diagonal and secondary diagonal
        matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]


def main() -> None:
    """
    Main function to read input, swap the diagonals, and print the result.
    """
    n: int = int(input())  # Number of rows/columns of the square matrix
    matrix: List = [input().split() for _ in range(n)]

    swap_diagonals(matrix, n)

    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
