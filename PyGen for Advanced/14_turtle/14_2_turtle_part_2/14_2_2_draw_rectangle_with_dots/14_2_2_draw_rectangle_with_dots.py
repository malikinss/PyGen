'''
TODO:
    Write a program that draws a rectangle with a dot at each corner.
'''
import turtle


def draw_rectangle_with_dots(
    width: int, height: int, dot_size: int = 10
) -> None:
    """
    Draws a rectangle with a dot at each corner.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        dot_size (int, optional): The size of the dot. Default is 10.
    """
    for _ in range(2):
        turtle.forward(width)  # Draw the top or bottom side
        turtle.dot(dot_size)   # Place a dot at the corner
        turtle.left(90)        # Turn 90 degrees
        turtle.forward(height)  # Draw the side
        turtle.dot(dot_size)   # Place a dot at the corner
        turtle.left(90)        # Turn 90 degrees


# Call the function to draw a rectangle with dots at the corners
draw_rectangle_with_dots(100, 50)
