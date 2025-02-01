'''
TODO:
    Write a program that draws a picture of a house using a sample.
'''
import turtle


def draw_shape(sides: int, length: int, angle: int, color: tuple):
    """
    Draws a filled polygon (like a house) with given parameters.

    Args:
        sides (int): Number of sides for the polygon.
        length (int): Length of each side of the polygon.
        angle (int): Angle for turning at each corner of the polygon.
        color (tuple): RGB color values for filling the shape.
    """
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(angle)
    turtle.end_fill()
    turtle.forward(20)
    turtle.right(90)


def draw_house():
    turtle.speed(0)
    turtle.hideturtle()

    # Draw the body and roof of the house using predefined values
    draw_shape(4, 120, 90, (185, 122, 87))  # House body
    draw_shape(3, 120, 120, (0, 162, 232))  # House roof


# Run the drawing function
draw_house()
