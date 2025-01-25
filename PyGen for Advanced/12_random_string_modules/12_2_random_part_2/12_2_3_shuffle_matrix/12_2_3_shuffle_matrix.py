'''
TODO:
    Write a program that uses the random module to randomly shuffle the
    contents of a matrix (two-dimensional list).

NOTE:
    There is no need to print the contents of the matrix.
'''
import random
from typing import List


def shuffle_matrix(matrix: List[List[int]]) -> None:
    """
    Randomly shuffles the contents of a matrix (two-dimensional list).

    Args:
        matrix (List[List[int]]): The matrix to shuffle, represented as a list
                                  of lists of integers.

    Returns:
        None
    """
    for row in matrix:
        random.shuffle(row)
    random.shuffle(matrix)
