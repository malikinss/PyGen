'''
TODO:
    Write a draw_triangle() function that draws a star right triangle with
    legs equal to 10
'''


def draw_triangle() -> None:
    """
    Draws a right triangle using stars with legs of length 10.
    The first row has 1 star, the second row has 2 stars, and so on
    until the 10th row which contains 10 stars.

    Example Output:
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********

    Returns:
    None
    """
    print(*['*' * i for i in range(1, 11)], sep='\n')


# Example usage
draw_triangle()
