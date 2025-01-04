'''
TODO:
    Two natural numbers n and m are given as input to the program.

    Write a program that creates an n*m matrix, filling it with "diagonals"
    according to the pattern.
        n = 3
        m = 5

        1  2  4  7  10
        3  5  8  11 13
        6  9  12 14 15
'''
from typing import List, Tuple


def get_matrix_size() -> Tuple[int, int]:
    """
    Reads the size of the matrix from user input.

    Returns:
        Tuple[int, int]: The number of rows (n) and columns (m) for the matrix.
    """
    n, m = map(int, input().split())
    return n, m


def create_empty_matrix(n: int, m: int) -> List[List[int]]:
    """
    Creates an empty matrix of size n*m, filled with zeros.

    Args:
        n (int): The number of rows in the matrix.
        m (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: An n*m matrix filled with zeros.
    """
    return [[0] * m for _ in range(n)]


def fill_diagonals(matrix: List[List[int]], n: int, m: int) -> List[List[int]]:
    """
    Fills the matrix diagonally according to the specified pattern.

    Args:
        matrix (List[List[int]]): The matrix to fill.
        n (int): The number of rows in the matrix.
        m (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: The matrix filled with diagonal values.
    """
    counter = 1
    # Loop over all diagonals, starting from the first row or first column
    for diag in range(n + m - 1):  # Total number of diagonals
        # Determine the start row and column for this diagonal
        if diag < n:
            row = diag  # Starts from the top row
            col = 0     # Starts from the first column
        else:
            row = n - 1  # Starts from the last row
            col = diag - n + 1  # Moves to the next column

        # Fill the diagonal, moving down-right
        while row >= 0 and col < m:
            matrix[row][col] = counter
            counter += 1
            row -= 1
            col += 1

    return matrix


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Prints the matrix row by row.

    Args:
        matrix (List[List[int]]): The matrix to print.
    """
    for row in matrix:
        print(" ".join(map(str, row)))


def main() -> None:
    """
    Main function to drive the program. It reads matrix size, creates
    the matrix, fills it with diagonal values, and then prints the matrix.
    """
    # Step 1: Get matrix size from the user
    n, m = get_matrix_size()

    # Step 2: Create an empty matrix
    matrix = create_empty_matrix(n, m)

    # Step 3: Fill the matrix diagonally
    matrix = fill_diagonals(matrix, n, m)

    # Step 4: Print the resulting matrix
    print_matrix(matrix)


# Call the main function to execute the program
if __name__ == "__main__":
    main()
