'''
TODO:
    Write a program that draws the pattern shown in the figure.
'''
import turtle


def draw_rectangle(side: int) -> None:
    """
    Draws a rectangle by moving forward and turning 90 degrees twice.

    Args:
        side (int): The length of the side of the rectangle.
    """
    for _ in range(2):
        turtle.forward(side)  # Draw one side of the rectangle
        turtle.right(90)


def draw_spiral(initial_side: int, step: int) -> None:
    """
    Draws a spiral pattern by repeatedly drawing rectangles with decreasing
    side lengths.

    Args:
        initial_side (int): The side length of the first rectangle.
        step (int): The amount by which the side length is reduced for each
                    subsequent rectangle.
    """
    side = initial_side
    while side > 0:
        draw_rectangle(side)  # Draw the current rectangle
        side -= step          # Reduce the side length for the next rectangle


# Call the function to draw the spiral pattern
draw_spiral(150, 10)
