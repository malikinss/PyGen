'''
TODO:
    Implement a triangle() function using recursion that takes one argument:
        h is a natural number

    The function should output a star triangle with height h according to the
    following example:
        *
        **
        ***
        ****
        *****
        ...
'''


def triangle(h: int) -> None:
    """
    Prints a star triangle with a height of h.

    Args:
        h (int): The height of the triangle. Must be a natural number.

    Returns:
        None
    """
    def print_triangle_lines(current_height: int) -> None:
        """
        Prints lines of stars to form a triangle with the given height.

        Args:
            current_height (int): The current height of the triangle being
            printed.

        Returns:
            None
        """
        if current_height > 0:
            print_triangle_lines(current_height - 1)
            print('*' * current_height)

    print_triangle_lines(h)
