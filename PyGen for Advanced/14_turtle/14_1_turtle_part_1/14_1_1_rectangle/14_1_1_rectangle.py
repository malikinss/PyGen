'''
TODO:
    Write a program that draws a rectangle.

NOTE:
    The program should be written as a function rectangle(width, height),
    where width, height are the width and height of the rectangle.
'''
import turtle


def rectangle(width: int, height: int) -> None:
    """
    Draws a rectangle with the given width and height using Python's Turtle
    graphics module.

    Args:
        width (int): the width of the rectangle.
        height (int): the height of the rectangle.
    """
    if width <= 0 or height <= 0:
        print("Width and height must be positive values.")
        return

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(1)  # Set the turtle speed to slow

    # Draw the rectangle
    for _ in range(2):
        t.forward(width)  # Draw the width side
        t.left(90)         # Turn 90 degrees to the left
        t.forward(height)  # Draw the height side
        t.left(90)         # Turn 90 degrees to the left

    # Hide the turtle and keep the window open
    t.hideturtle()
    turtle.done()


# Call the function with example dimensions
rectangle(200, 100)
