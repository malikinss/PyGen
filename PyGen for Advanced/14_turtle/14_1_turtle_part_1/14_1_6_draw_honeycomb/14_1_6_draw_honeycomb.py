'''
TODO:
    Write a program that draws a honeycomb.

NOTE:
    Make sure the hexagon drawing function returns the turtle to its
    starting point.
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


def draw_honeycomb(side: int, rows: int, cols: int) -> None:
    """
    Draws a honeycomb pattern made of hexagons using the hexagon function.

    Args:
        side (int): the length of the side of each hexagon.
        rows (int): the number of rows in the honeycomb.
        cols (int): the number of columns in the honeycomb.
    """
    for row in range(rows):
        for col in range(cols):
            hexagon(side)  # Draw one hexagon
            turtle.forward(side)  # Move to the next position

        # Move to the next row
        turtle.backward(side * cols)  # Go back to the start of the row
        turtle.left(60)  # Rotate for the next row
        turtle.forward(side)  # Move up one row
        turtle.right(60)  # Correct the orientation


# Draw a honeycomb of hexagons with side length 50, 6 rows and 6 columns
draw_honeycomb(50, 6, 6)
