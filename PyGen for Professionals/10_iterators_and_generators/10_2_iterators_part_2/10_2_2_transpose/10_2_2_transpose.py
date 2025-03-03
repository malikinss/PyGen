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


def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    """
    Transpose a matrix.

    Args:
        matrix (List[List[Any]]): A matrix of arbitrary dimension

    Returns:
        List[List[Any]]: The transposed matrix
    """
    return [list(row) for row in zip(*matrix)]
