'''
TODO:
    Write a program that draws a snowflake made of 10 diamonds.
'''
import turtle


def draw_rhombus(side: int) -> None:
    """
    Draws a rhombus (diamond shape) with the given side length.

    Args:
        side (int): The length of each side of the rhombus.
    """
    for i in range(1, 5):
        turtle.forward(side)  # Draw one side of the rhombus
        turtle.right(120 - 60 * (i % 2))  # Turn 60 or 120 degrees


def draw_snowflake(diamonds: int, side: int) -> None:
    """
    Draws a snowflake made of diamonds.

    Args:
        diamonds (int): The number of diamonds to draw in the snowflake.
        side (int): The side length of each diamond.
    """
    for _ in range(diamonds):
        draw_rhombus(side)  # Draw a rhombus
        turtle.right(360 / diamonds)  # Rotate to the next position


# Call the function to draw a snowflake with 10 diamonds,
# each with side length 100
draw_snowflake(10, 100)
