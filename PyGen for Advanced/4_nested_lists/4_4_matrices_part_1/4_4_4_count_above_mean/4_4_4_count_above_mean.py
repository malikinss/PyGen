'''
TODO:
    Write a program that prints the number of elements of a square matrix
    in each row that are greater than the arithmetic mean of the elements
    of that row.
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


def count_above_mean(matrix: List[List[int]]) -> List[int]:
    """
    Counts the number of elements greater than the arithmetic mean in each row.

    Args:
        matrix (List[List[int]]): Square matrix.

    Returns:
        List[int]: List of counts for each row.
    """
    counts = []
    for row in matrix:
        row_mean = sum(row) / len(row)
        count = sum(1 for element in row if element > row_mean)
        counts.append(count)
    return counts


def main() -> None:
    """
    Main function to read input, compute the counts, and print the result.
    """
    n: int = int(input())
    matrix = read_square_matrix(n)

    for count in count_above_mean(matrix):
        print(count)


if __name__ == "__main__":
    main()
