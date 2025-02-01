'''
TODO:
    Write a matrix() function that creates, fills, and returns a matrix of
    a given size.

    Depending on the arguments passed, it should behave like this:
        - matrix() — returns a 1*1 matrix in which the only number is zero;
        - matrix(n) — returns an n * n matrix filled with zeros;
        - matrix(n, m) — returns a matrix of n rows and m columns filled
                         with zeros;
        - matrix(n, m, value) — returns a matrix of n rows and m columns
                                in which each element is equal to the number
                                value.

    Use default arguments when creating a function.

NOTE:
    The code below:
        print(matrix()) # matrix 1 * 1 of 0
        print(matrix(3)) # matrix 3 * 3 of 0
        print(matrix(2, 5)) # matrix 2 * 5 of 0
        print(matrix(3, 4, 9)) # matrix 3 * 4 of 9
    should output:
        [[0]]
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        [[0, 0, 0, 0, 0], [0, 0, 0, 0]]
        [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]

    You don't need to call matrix(), you just need to implement it.
'''
from typing import Any, Union, List


def matrix(
    n: int = 1,
    m: Union[int, None] = None,
    value: Any = 0
) -> List[List[Any]]:
    """
    Creates and returns a matrix of given size and fills it with a specified
    value.

    Args:
        n (int, optional): Number of rows. Defaults to 1.
        m (Union[int, None], optional): Number of columns. Defaults to None,
                                        which makes it equal to n.
        value (Any, optional): Value to fill the matrix. Defaults to 0.

    Returns:
        List[List[Any]]: A matrix (list of lists) of size n*m filled
                         with `value`.
    """
    if m is None:
        m = n

    return [[value] * m for _ in range(n)]
