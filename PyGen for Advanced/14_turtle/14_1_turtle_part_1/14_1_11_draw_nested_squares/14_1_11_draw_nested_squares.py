'''
TODO:
    Write a program that draws squares to create the pattern shown
    in the figure.
'''
import turtle


def draw_square(side: int) -> None:
    """
    Draws a square of a given side length using Python's Turtle graphics
    module.

    Args:
        side (int): The length of the side of the square.
    """
    for _ in range(4):
        turtle.forward(side)  # Draw one side of the square
        turtle.right(90)       # Turn 90 degrees to form the square's corners


def draw_nested_squares(initial_side: int, step: int) -> None:
    """
    Draws a series of nested squares, where each subsequent square has
    a side length reduced by the given step.

    Args:
        initial_side (int): The side length of the first square.
        step (int): The amount by which the side length is reduced for each
                    subsequent square.
    """
    side = initial_side
    for _ in range(9):
        draw_square(side)  # Draw the current square
        side -= step       # Reduce the side length for the next square


# Call the function to draw the nested squares pattern
draw_nested_squares(100, 10)
