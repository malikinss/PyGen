'''
TODO:
    Write a draw_triangle(fill, base) function that takes two parameters:
        - fill is a fill character;
        - base - the value of the base of an isosceles triangle;

    and then outputs it.

NOTE:
    It is guaranteed that the base of the triangle is an odd number.
'''


def draw_triangle(fill: str, base: int) -> None:
    """
    Draws an isosceles triangle using the given fill character and base length.

    The function generates a triangle where:
    - The `fill` parameter is used to fill the triangle.
    - The `base` parameter defines the base width, which is guaranteed to
    be an odd number.

    Example:
    For fill = '*' and base = 7:
        *
       ***
      *****
     *******
    *********

    Args:
    fill (str): The character used to fill the triangle.
    base (int): The base length of the isosceles triangle (an odd number).

    Returns:
    None
    """
    # Loop through each row of the triangle
    for i in range(1, base + 1, 2):
        # Print the correct number of characters for the current row
        spaces = (base - i) // 2  # Calculate leading spaces
        print(' ' * spaces + fill * i)


# Example usage:
fill = input()
base = int(input())

draw_triangle(fill, base)
