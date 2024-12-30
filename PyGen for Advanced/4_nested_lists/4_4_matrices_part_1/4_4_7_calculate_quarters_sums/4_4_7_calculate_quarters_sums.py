'''
TODO:
    A square matrix is divided into four quarters, bounded by the main
    and secondary diagonals:
        upper, lower, left and right.

    Write a program that calculates the sum of the elements:
        - upper quarter;
        - right quarter;
        - lower quarter;
        - left quarter.
'''
from typing import List, Tuple


def read_square_matrix(n: int) -> List[List[int]]:
    """
    Reads an n x n square matrix from user input.

    Args:
        n (int): Size of the square matrix.

    Returns:
        List[List[int]]: Square matrix as a list of lists of integers.
    """
    return [list(map(int, input().split())) for _ in range(n)]


def calculate_quarters_sums(
    matrix: List[List[int]]
) -> Tuple[int, int, int, int]:
    """
    Calculates the sums of the four quarters of a square matrix.

    Args:
        matrix (List[List[int]]): Square matrix.

    Returns:
        Tuple[int, int, int, int]: Sums of the upper, right, lower, and
        left quarters.
    """
    n = len(matrix)
    up_sum = right_sum = down_sum = left_sum = 0

    for i in range(n):
        for j in range(n):
            if i < j and i < n - 1 - j:
                up_sum += matrix[i][j]
            if i < j and i > n - 1 - j:
                right_sum += matrix[i][j]
            if i > j and i > n - 1 - j:
                down_sum += matrix[i][j]
            if i > j and i < n - 1 - j:
                left_sum += matrix[i][j]

    return up_sum, right_sum, down_sum, left_sum


def main() -> None:
    """
    Main function to read input, compute sums of quarters, and print
    the results.
    """
    n: int = int(input())
    matrix = read_square_matrix(n)
    up, right, down, left = calculate_quarters_sums(matrix)

    print(f"""upper quarter: {up}
right quarter: {right}
lower quarter: {down}
left quarter: {left}""")


if __name__ == "__main__":
    main()
