'''
TODO:
    Write a program that outputs the maximum element in the region located
    to the right of the secondary diagonal of a square matrix.

    Elements of the secondary diagonal are also taken into account.
        0 0 0 0 *
        0 0 0 * *
        0 0 * * *
        0 * * * *
        * * * * *
'''
from typing import List


def get_matrix(n: int) -> List[List[int]]:
    """
    Reads a square matrix of size n from user input.

    Args:
        n (int): Size of the matrix (n x n).

    Returns:
        List[List[int]]: The square matrix of integers.
    """
    matrix = []
    for _ in range(n):
        # Read each row, split by space, and convert to integers
        matrix.append(list(map(int, input().split())))
    return matrix


def find_max_in_secondary_diagonal_region(
    matrix: List[List[int]], n: int
) -> int:
    """
    Finds the maximum element in the region to the right of the secondary
    diagonal of a square matrix, including the diagonal itself.

    Args:
        matrix (List[List[int]]): Square matrix of integers.
        n (int): Size of the matrix (n x n).

    Returns:
        int: Maximum element in the specified region.
    """
    # Initialize maximum with the top-right corner element
    maximum = matrix[0][n - 1]

    # Iterate over the matrix, focusing on the region right
    # of the secondary diagonal
    for i in range(n):
        for j in range(n - i - 1, n):
            # Update the maximum if a larger element is found
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

    return maximum


def main() -> None:
    """
    Main function to handle input, compute the maximum, and print the result.
    """
    # Read matrix size
    n = int(input("Enter the size of the square matrix: "))

    # Get the matrix from user input
    matrix = get_matrix(n)

    # Find the maximum element in the required region
    result = find_max_in_secondary_diagonal_region(matrix, n)

    # Print the result
    print(result)


if __name__ == "__main__":
    main()
