'''
TODO:
    Write a program that swaps columns in a matrix.
'''
from typing import List


def swap_columns(
    n: int, matrix: List[List[int]], col_indices: List[int]
) -> List[List[int]]:
    """
    Swaps two columns in the matrix.

    Args:
        n (int): The number of rows in the matrix.
        matrix (List[List[int]]): The matrix to operate on.
        col_indices (List[int]): A list containing two indices of columns
                                 to swap.

    Returns:
        List[List[int]]: The matrix after the columns are swapped.
    """
    a, b = col_indices[0], col_indices[1]
    for i in range(n):
        matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
    return matrix


def main() -> None:
    """
    Main function to read input, swap columns, and print the modified matrix.
    """
    n: int = int(input())  # Number of rows

    matrix: List[List[int]] = [
        list(map(int, input().split())) for _ in range(n)
    ]
    col_indices: List[int] = list(map(int, input().split()))

    swapped_matrix = swap_columns(n, matrix, col_indices)

    for row in swapped_matrix:
        print(*row)


if __name__ == "__main__":
    main()
