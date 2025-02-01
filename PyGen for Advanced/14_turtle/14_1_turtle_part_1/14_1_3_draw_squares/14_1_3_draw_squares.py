'''
TODO:
    Write a program that draws a figure consisting of three squares.

NOTE:
    Write a function square(side), where side is the length of the square's
    side in pixels.

    Experiment with the angle of rotation of the turtle when moving from
    one square to another.
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


def draw_squares(side: int, num_squares: int) -> None:
    """
    Draws a figure consisting of multiple squares.

    Args:
        side (int): the length of the side of each square.
        num_squares (int): the number of squares to draw.
    """
    for i in range(num_squares):
        square(side)
        turtle.left(360 / num_squares)


side = int(input("Enter the side length of the squares: "))

draw_squares(side, 3)  # Draw three squares
