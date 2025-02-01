'''
TODO:
    Write a program that draws a star at the click location when the left
    mouse button is pressed.

    The background of the image should be black, and the stars can be of
    different sizes, colors, and have a different number of sides.
'''
import turtle as t
from math import sin, cos, radians, log2
from random import randrange as rnd


def random_color() -> tuple[int, int, int]:
    """
    Generates a random RGB color.

    Returns:
        tuple: A tuple containing three integers (R, G, B) each in the range
               [0, 255].
    """
    return rnd(256), rnd(256), rnd(256)


def draw_uneven_star(
    obj: t.Turtle,
    beams: int,
    figures: int,
    i: int,
    coors: tuple[int, int],
    r: int,
    col: tuple[int, int, int]
) -> None:
    """
    Draws an uneven star with specified beams and figures at given coordinates.

    Args:
        obj (t.Turtle): The turtle object used to draw.
        beams (int): The number of beams (points) in the star.
        figures (int): The number of figures (usually powers of 2).
        i (int): The index for the current figure.
        coors (tuple[int, int]): The (x, y) coordinates for the center
                                 of the star.
        r (int): The radius of the star.
        col (tuple[int, int, int]): The color of the star in RGB format.
    """
    angle = 360 / beams / figures * i
    obj.right(angle)

    val = radians(180 / beams / 2 + angle)
    x_start = coors[0] - r * cos(val)
    y_start = coors[1] + r * sin(val)

    w = 2 * r * cos(radians(180 / beams / 2))
    obj.up()
    obj.goto(x_start, y_start)
    obj.down()
    obj.color(col)
    obj.begin_fill()
    for _ in range(beams):
        obj.forward(w)
        obj.right(180 - 180 / beams)
    obj.end_fill()
    obj.setheading(0)


def draw_square(
    obj: t.Turtle,
    beams: int,
    figures: int,
    i: int,
    coors: tuple[int, int],
    r: int,
    col: tuple[int, int, int]
) -> None:
    """
    Draws a square-like star with 4 beams at given coordinates.

    Args:
        obj (t.Turtle): The turtle object used to draw.
        beams (int): The number of beams (4 for squares).
        figures (int): The number of figures (usually 1 for squares).
        i (int): The index for the current figure.
        coors (tuple[int, int]): The (x, y) coordinates for the center
        of the star.
        r (int): The radius of the star.
        col (tuple[int, int, int]): The color of the star in RGB format.
    """
    angle = 360 / beams / figures * i
    obj.right(angle)
    x_start = coors[0] - r * cos(radians(45 + angle))
    y_start = coors[1] + r * sin(radians(45 + angle))

    w = 2 * r / 2 ** 0.5
    obj.up()
    obj.goto(x_start, y_start)
    obj.down()
    obj.color(col)
    obj.begin_fill()
    for _ in range(4):
        obj.forward(w)
        obj.right(90)
    obj.end_fill()
    obj.setheading(0)


def draw_star(
    obj: t.Turtle,
    beams: int,
    coors: tuple[int, int],
    r: int,
    col: tuple[int, int, int]
) -> None:
    """
    Draws a star with the specified number of beams, size, and color.

    Args:
        obj (t.Turtle): The turtle object used to draw the star.
        beams (int): The number of beams (points) of the star.
        coors (tuple[int, int]): The (x, y) coordinates for the center
                                 of the star.
        r (int): The radius of the star.
        col (tuple[int, int, int]): The color of the star in RGB format.
    """
    while beams % 2 == 0 and beams != 4:
        beams //= 2

    figures = 2 ** int(log2(beams)) if beams != 4 else 1
    draw_function = draw_square if beams == 4 else draw_uneven_star

    for i in range(figures):
        draw_function(obj, beams, figures, i, coors, r, col)


def left_mouse_click(x: int, y: int) -> None:
    """
    Callback function for handling left mouse click event.

    Args:
        x (int): The x-coordinate of the click.
        y (int): The y-coordinate of the click.
    """
    draw_star(
        obj=t,  # type: ignore
        beams=rnd(5, 33),
        coors=(x, y),
        r=rnd(15, 40),
        col=random_color()
    )


# Set up screen
t.Screen().bgcolor('black')
t.Screen().colormode(255)
t.hideturtle()
t.speed(0)

# Set up event listener for left mouse clicks
t.Screen().onclick(left_mouse_click)    # type: ignore
t.Screen().listen()

t.done()
