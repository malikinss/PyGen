'''
TODO:
    You have access to the generator function matrix_by_elem(), which takes
    a matrix of arbitrary dimensions as an argument and returns a generator
    that produces a sequence of elements of the given matrix.

    Rewrite this function using the yield from construct to perform
    the same task.

NOTE:
    Matrix refers exclusively to nested lists.
'''
from typing import List, Generator


def matrix_by_elem(
    matrix: List[List[int | float]]
) -> Generator[int | float, None, None]:
    """
    Generates a sequence of elements from a matrix.

    Args:
        matrix (List[List[int | float]]): A matrix represented as a list
        of lists, where each element is either an integer or a float.

    Yields:
        int | float: Each element of the matrix, one by one, in the order
                     they appear row by row.
    """
    for row in matrix:
        yield from row
