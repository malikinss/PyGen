'''
TODO:
    Write a function draw_triangle() that draws a star isosceles triangle with
    base and height equal to 15 and 8 respectively:
'''


def draw_triangle() -> None:
    """
    Draws an isosceles triangle with a base of 15 stars and a height of 8.

    The triangle is centered horizontally, with the base consisting of 15 stars
    and the height consisting of 8 rows. Each row has an odd number of stars,
    starting from 1 at the top row and increasing by 2 stars until
    the base is reached.

    Returns:
        None: This function does not return any value.
              It prints the triangle to the console.
    """
    height = 8  # The height of the triangle
    base = 15    # The base of the triangle

    for i in range(1, height + 1):
        # Calculate the number of stars for the current row
        num_stars = 2 * i - 1
        # Calculate the number of leading spaces for the current row
        num_spaces = (base - num_stars) // 2
        # Print the row with spaces and stars
        print(' ' * num_spaces + '*' * num_stars)


draw_triangle()
