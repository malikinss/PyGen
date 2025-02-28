'''
TODO:
    Implement a triangle() function using recursion that takes one argument:
        h is a natural number

    The function should output a star triangle with height h according to the
    following example:
        ...
        *****
        ****
        ***
        **
        *
'''


def triangle(h: int) -> None:
    """
    Print a star triangle with height h.

    Args:
        h (int): The height of the triangle.

    Returns:
        None
    """
    if h > 0:
        print('*' * h)
        triangle(h - 1)
