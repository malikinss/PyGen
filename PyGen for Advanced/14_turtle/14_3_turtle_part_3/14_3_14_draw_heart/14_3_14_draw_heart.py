'''
TODO:
    Write a program that draws an image of a heart using a sample.

    Such a figure is defined parametrically in the form:
        x = 128*sin(t)**3
        y = 8*(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t) - 5)
    where t∈[0;2π] is a parameter.

NOTE:
    Change the value of the t parameter in small steps of 0.01.

    To move the turtle to a given point, use the goto(x, y) command.
'''
import turtle
from math import sin, cos


def setup_turtle(
    pen_size: int, color: str, hide: bool = True
) -> turtle.Turtle:
    """
    Setup the turtle with specific settings.

    Args:
        pen_size (int): The size of the pen used for drawing.
        color (str): The color of the pen.
        hide (bool, optional): Whether to hide the turtle cursor.
                               Defaults to True.

    Returns:
        turtle.Turtle: The configured turtle instance.
    """
    t = turtle.Turtle()
    t.pensize(pen_size)
    t.color(color)
    if hide:
        t.hideturtle()
    return t


def draw_arrow() -> None:
    """
    Draws an arrow shape and places a stamp at a specific position.
    """
    arrow_turtle = setup_turtle(5, 'black', hide=False)
    arrow_turtle.up()
    arrow_turtle.goto(0, -50)
    arrow_turtle.down()
    arrow_turtle.left(45)
    arrow_turtle.forward(150)
    arrow_turtle.left(180)
    arrow_turtle.forward(50)
    arrow_turtle.left(180)
    for _ in range(5):
        x, y = arrow_turtle.pos()
        arrow_turtle.left(45)
        arrow_turtle.forward(15)
        arrow_turtle.goto(x, y)
        arrow_turtle.right(90)
        arrow_turtle.forward(15)
        arrow_turtle.goto(x, y)
        arrow_turtle.left(45)
        arrow_turtle.forward(10)
    arrow_turtle.up()
    arrow_turtle.goto(-56, -106)
    arrow_turtle.left(180)
    arrow_turtle.down()
    arrow_turtle.forward(60)
    arrow_turtle.shape('arrow')
    arrow_turtle.stamp()


def calculate_heart_coordinates(t: float) -> tuple:
    """
    Calculates the coordinates (x, y) for the parametric heart shape.

    Args:
        t (float): The parameter for the parametric equation.

    Returns:
        tuple: The calculated (x, y) coordinates.
    """
    x = 128 * sin(t) ** 3
    y = 8 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t) - 5)
    return x, y


def draw_heart() -> None:
    """
    Draws a filled heart shape using a parametric equation.
    """
    heart_turtle = setup_turtle(2, 'red', hide=False)
    heart_turtle.fillcolor('red')
    heart_turtle.begin_fill()

    # Parametric equation for the heart
    for t in range(630):
        t *= 0.01   # type: ignore
        x, y = calculate_heart_coordinates(t)
        heart_turtle.goto(x, y)

    heart_turtle.end_fill()


draw_heart()
draw_arrow()
