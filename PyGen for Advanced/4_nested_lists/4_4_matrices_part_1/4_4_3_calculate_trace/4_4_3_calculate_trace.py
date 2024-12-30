'''
TODO:
    The trace of a square matrix is the sum of the elements
    of the main diagonal.

    Write a program that outputs the trace of a given square matrix.
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


def calculate_trace(matrix: List[List[int]]) -> int:
    """
    Calculates the trace of a square matrix (sum of the main diagonal elements)

    Args:
        matrix (List[List[int]]): Square matrix.

    Returns:
        int: Trace of the matrix.
    """
    return sum(matrix[i][i] for i in range(len(matrix)))


def main() -> None:
    """
    Main function to read input, compute the trace, and print the result.
    """
    n: int = int(input())
    matrix = read_square_matrix(n)
    print(calculate_trace(matrix))


if __name__ == "__main__":
    main()
