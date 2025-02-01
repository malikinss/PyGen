'''
TODO:
    Write a program that draws a rhombus with angles of 60 and 120 degrees.
'''
import turtle


def draw_rhombus(side: int) -> None:
    """
    Draws a rhombus with angles of 60 and 120 degrees using the given
    side length.

    Args:
        side (int): the length of the side of the rhombus.
    """
    for i in range(2):
        turtle.forward(side)  # Draw the first side of the rhombus
        turtle.left(60)        # Turn by 60 degrees
        turtle.forward(side)  # Draw the opposite side
        turtle.left(120)       # Turn by 120 degrees for the next side


# Example usage
draw_rhombus(100)
