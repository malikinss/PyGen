'''
TODO:
    Write a program that draws a Star of David.

    This star can be created from two triangles.

    However, they cannot be drawn as a continuous line, so the pen must be
    lifted to move to the second triangle.
'''
import turtle


def draw_star_of_david(size: int) -> None:
    """
    Draws the Star of David using two overlapping equilateral triangles.

    Args:
        size (int): The length of each side of the triangles.
    """
    for _ in range(3):  # Draw the first triangle
        turtle.forward(size)
        turtle.left(120)

    # Move to the starting point for the second triangle
    turtle.penup()
    turtle.forward(size / 3)
    turtle.left(120)
    turtle.forward(size / 3 * 2)
    turtle.right(120)
    turtle.pendown()

    for _ in range(3):  # Draw the second triangle
        turtle.forward(size)
        turtle.right(120)


# Example usage
draw_star_of_david(100)
