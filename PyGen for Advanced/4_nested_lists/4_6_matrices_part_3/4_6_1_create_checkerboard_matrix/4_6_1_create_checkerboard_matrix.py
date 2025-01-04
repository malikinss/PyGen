'''
TODO:
    The program is given two natural numbers n and m as input.

    Write a program to create a matrix of size n*m, filling it
    with the symbols . and * in a checkerboard pattern.

    There should be a dot in the upper left corner.

    Display the resulting matrix on the screen, separating the elements
    with spaces.
'''


def create_checkerboard_matrix(rows, columns):
    """Generate a checkerboard matrix with '.' and '*' symbols."""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            # Determine the symbol based on the row and column index
            if (i + j) % 2 == 0:
                row.append(".")
            else:
                row.append("*")
        matrix.append(row)
    return matrix


def get_matrix_size():
    """Parse the matrix size from the input."""
    return map(int, input().split())


def print_matrix(matrix):
    """Print the matrix row by row."""
    for row in matrix:
        print(*row)


# Main logic
n, m = get_matrix_size()  # Get rows and columns
matrix = create_checkerboard_matrix(n, m)  # Generate the matrix
print_matrix(matrix)  # Print the matrix
