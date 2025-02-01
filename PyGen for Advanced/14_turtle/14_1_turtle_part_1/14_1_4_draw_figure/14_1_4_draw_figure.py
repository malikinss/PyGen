'''
TODO:
    Write a program that draws a figure made of eight squares.
'''
import turtle


def square(side: int) -> None:
    """
    Draws a square with the given side length using Python's Turtle
    graphics module.

    Args:
        side (int): the length of the side of the square.
    """
    for _ in range(4):
        turtle.forward(side)  # Draw one side of the square
        turtle.left(90)        # Turn 90 degrees to form the square's angles


def draw_figure(num_squares: int, side: int) -> None:
    """
    Draws a figure consisting of multiple squares.

    Args:
        num_squares (int): the number of squares to draw.
        side (int): the length of the side of each square.
    """
    for _ in range(num_squares):
        square(side)            # Draw a square
        turtle.left(360 / num_squares)


draw_figure(8, 120)  # Draw a figure made of 8 squares
