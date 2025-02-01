'''
TODO:
    Write a program that draws an image of the Olympic symbol.
'''
import turtle


def move_to(x: int, y: int) -> None:
    """
    Moves the turtle to a specified location without drawing.

    Args:
        x (int): X-coordinate.
        y (int): Y-coordinate.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_olympic_rings() -> None:
    """
    Draws the Olympic rings using Turtle graphics.
    """
    turtle.speed(0)
    turtle.pensize(5)

    colors = ['deepskyblue', 'black', 'red', 'yellow', 'chartreuse']
    coords = [(-110, 0), (0, 0), (110, 0), (-55, -50), (55, -50)]

    for color, (x, y) in zip(colors, coords):
        turtle.pencolor(color)
        move_to(x, y)
        turtle.circle(50)


# Example usage
draw_olympic_rings()
