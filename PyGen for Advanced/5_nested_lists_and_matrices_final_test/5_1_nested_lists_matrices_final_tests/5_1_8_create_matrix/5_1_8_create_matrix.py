'''
TODO:
    The input to the program is a natural number n.

    Write a program that creates a matrix of size n*n and fills it according
    to the following rule:
        - on the main diagonal, the number 0 should be in place
          of each element;
        - on the two diagonals adjacent to the main one - the number 1;
        - on the next two diagonals - the number 2, etc.
'''
from typing import List


def create_matrix(n: int) -> List[List[int]]:
    """
    Creates a matrix of size n*n, filling it according to the specified rule:
    - 0 on the main diagonal
    - 1 on the diagonals adjacent to the main diagonal
    - 2 on the next two diagonals, and so on.

    Args:
        n (int): Size of the matrix (n x n).

    Returns:
        List[List[int]]: The generated matrix.
    """
    return [[abs(i - j) for j in range(n)] for i in range(n)]


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Prints the matrix row by row.

    Args:
        matrix (List[List[int]]): The matrix to print.
    """
    for row in matrix:
        print(' '.join(map(str, row)))


def main() -> None:
    """
    Main function to read input, generate the matrix, and print the result.
    """
    n = int(input("Enter the size of the matrix (n): "))
    matrix = create_matrix(n)
    print_matrix(matrix)


if __name__ == "__main__":
    main()
