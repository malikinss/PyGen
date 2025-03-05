'''
TODO:
    A transposed matrix is a matrix A^T obtained from the original matrix A by
    replacing rows with columns.

    For example, if original matrix:
        [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]
    then transposed matrix:
        [1, 4, 7]
        [2, 5, 8]
        [3, 6, 9]

    That is, to obtain a transposed matrix from the original, you need to
    write each row of the original matrix as a column in the same order.

    Implement the transpose() function using the zip() function, which takes
    one argument:
        matrix - a matrix of arbitrary dimension

    The function must return the transposed matrix.

NOTE:
    Matrix means only nested lists.
    The function must return a new matrix, not modify the passed one.
'''
from typing import List, Any

Matrix = List[List[Any]]


def transpose(matrix: Matrix) -> Matrix:
    """
    Transpose a matrix, switching rows with columns.

    Args:
        matrix (Matrix): A matrix of arbitrary dimension, represented
        as a list of lists.

    Returns:
        Matrix: The transposed matrix, with rows and columns swapped.
    """
    # Using zip to group elements of the original matrix by columns
    # and convert each group into a list
    return [list(row) for row in zip(*matrix)]


# Example usage
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose(original_matrix)
print(transposed_matrix)
