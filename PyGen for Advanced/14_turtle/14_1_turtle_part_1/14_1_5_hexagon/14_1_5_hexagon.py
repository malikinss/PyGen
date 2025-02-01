'''
TODO:
    Write a program that draws a regular hexagon.

NOTE:
    The program should be written as a function hexagon(side),
    where side is the length of the side in pixels.

    The size of each angle of a regular hexagon is 120 degrees.
'''
import turtle


def hexagon(side: int) -> None:
    """
    Draws a regular hexagon with the given side length using Python's Turtle
    graphics module.

    Args:
        side (int): the length of the side of the hexagon.
    """
    for _ in range(6):
        turtle.forward(side)  # Draw one side of the hexagon
        turtle.left(60)        # Turn 60 degrees to form the hexagon's angles


hexagon(100)  # Call the function to draw a hexagon with side length 100
