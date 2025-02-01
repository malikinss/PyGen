'''
TODO:
    Write a program that draws a picture of a teddy bear.
'''
import turtle


def draw_circle(
    x: int, y: int, radius: int, fill: bool = False
) -> None:
    """
    Draws a circle at a given position.

    Args:
        x (int): X-coordinate.
        y (int): Y-coordinate.
        radius (int): Radius of the circle.
        fill (bool): Whether to fill the circle.
    """
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    if fill:
        turtle.begin_fill()
    turtle.circle(radius)
    if fill:
        turtle.end_fill()


def draw_head() -> None:
    """Draws the teddy bear's head and snout."""
    draw_circle(0, 0, 150)  # Head
    draw_circle(0, -30, 75)  # Snout


def draw_ears() -> None:
    """Draws the teddy bear's ears."""
    positions = [(-125, 150), (125, 150)]
    for x, y in positions:
        draw_circle(x, y, 30)


def draw_eyes() -> None:
    """Draws the teddy bear's eyes."""
    turtle.color('black')
    positions = [(-50, 50), (50, 50)]
    for x, y in positions:
        draw_circle(x, y, 10, fill=True)


def draw_nose() -> None:
    """Draws the teddy bear's nose."""
    turtle.color('black')
    draw_circle(0, 20, 15, fill=True)


def draw_teddy_bear() -> None:
    """Draws the complete teddy bear."""
    turtle.speed(0)
    turtle.color('brown')

    draw_head()
    draw_ears()
    draw_eyes()
    draw_nose()

    turtle.hideturtle()
    turtle.done()


# Example usage
draw_teddy_bear()
