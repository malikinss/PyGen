'''
TODO:
    A magic square of order n is a square matrix of size n*n,
    composed of all the numbers 1,2,3, …, n^2, such that the sums
    for each column, each row, and each of the two diagonals are equal.

    Write a program that checks whether a given square matrix is
    a magic square.
'''


def is_magic_square(matrix: list[list[int]]) -> bool:
    """Check if a given square matrix is a magic square.

    Args:
        matrix (list[list[int]]): Square matrix to check.

    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    n = len(matrix)

    # Create a list of expected digits (1 to n^2)
    expected_digits = list(range(1, n**2 + 1))

    # Calculate the control sum based on the main diagonal
    control_sum = sum(matrix[i][i] for i in range(n))

    # Initialize diagonal sums
    main_diagonal, anti_diagonal = 0, 0

    # Iterate through each row and column
    for i in range(n):
        row_sum, col_sum = 0, 0
        for j in range(n):
            # Calculate the sums of the current row and column
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]

            # Check if the matrix element is in the expected list
            if matrix[i][j] in expected_digits:
                expected_digits.remove(matrix[i][j])

        # Calculate the sums of the main and anti-diagonals
        main_diagonal += matrix[i][i]
        anti_diagonal += matrix[i][n - i - 1]

        # If any row or column sum does not match the control sum, return False
        if row_sum != control_sum or col_sum != control_sum:
            return False

    # Final check: diagonals must match control sum
    # and all numbers 1 to n^2 must be present
    expression = control_sum == main_diagonal == anti_diagonal
    return expression and not expected_digits


# Read input and construct the matrix
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Print the result
print('YES' if is_magic_square(matrix) else 'NO')
