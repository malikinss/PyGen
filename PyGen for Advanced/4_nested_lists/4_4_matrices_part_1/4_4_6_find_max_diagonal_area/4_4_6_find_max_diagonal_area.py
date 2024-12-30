'''
TODO:
    Write a program that prints the maximum element to the right and left
    of the main and secondary diagonals of a square matrix.

NOTE:
    The elements of the diagonals are also taken into account.
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


def find_max_diagonal_area(matrix: List[List[int]]) -> int:
    """
    Finds the maximum element to the left and right of the main
    and secondary diagonals.

    Args:
        matrix (List[List[int]]): Square matrix.

    Returns:
        int: Maximum element from the specified areas.
    """
    n = len(matrix)
    selected_elements = []

    for i in range(n):
        for j in range(n):
            # Conditions to select elements on and around both diagonals
            if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
                selected_elements.append(matrix[i][j])

    return max(selected_elements)


def main() -> None:
    """
    Main function to read input, compute the maximum, and print the result.
    """
    n: int = int(input())
    matrix = read_square_matrix(n)

    print(find_max_diagonal_area(matrix))


if __name__ == "__main__":
    main()
