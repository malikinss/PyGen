'''
TODO:
    Write a program that draws the solar system using a sample.
'''
import turtle
from random import randint

# Constants
FONT: tuple[str, int, str] = ('Arial', 8, 'normal')
ZOOM: float = 0.6
PITCH: int = 18
PLANETS: list[tuple[str, float, str]] = [
    ('Солнце', 1390, 'yellow'),
    ('Меркурий', 4.8794, '#8A8784'),
    ('Венера', 12.1036, '#D08824'),
    ('Земля', 12.742, '#6082CA'),
    ('Марс', 6.78, '#BF9A76'),
    ('Юпитер', 139.822, '#BAB9C3'),
    ('Сатурн', 116.464, '#D9AB47'),
    ('Уран', 50.724, '#60BDEE'),
    ('Нептун', 49.244, '#4C6DED'),
    ('Плутон', 2.3766, '#5B5D5A')
]


def draw_ellipse(rad: int) -> None:
    """
    Draws an elliptical orbit.

    Args:
        rad (int): The radius of the ellipse.
    """
    for _ in range(2):
        turtle.circle(rad - 90, 90)
        turtle.circle(rad // 2 - 90, 90)


def draw_starfield(num_stars: int) -> None:
    """
    Draws random stars in the background.

    Args:
        num_stars (int): The number of stars to draw.
    """
    turtle.pencolor('white')
    for _ in range(num_stars):
        turtle.penup()
        turtle.goto(randint(-500, 500), randint(-200, 200))
        turtle.pendown()
        turtle.circle(0.5)


def place_planet(name: str, size: float, color: str, x: float) -> None:
    """
    Draws a planet with its name.

    Args:
        name (str): The name of the planet.
        size (float): The size of the planet in thousands of km.
        color (str): The color of the planet.
        x (float): The x-coordinate for positioning.
    """
    scaled_size: float = size * ZOOM
    y: float = -scaled_size

    # Draw the planet
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.circle(scaled_size)
    turtle.end_fill()

    # Draw the planet name
    turtle.penup()
    turtle.goto(x, y - PITCH)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.write(name, align='center', font=FONT)


def setup_screen() -> None:
    """
    Configures the screen settings.
    """
    screen = turtle.Screen()
    screen.setup(1000, 400)
    screen.colormode(255)
    screen.bgcolor('black')


def setup_turtle() -> None:
    """
    Configures the turtle settings.
    """
    turtle.speed(0)
    turtle.hideturtle()


def draw_planets() -> None:
    """
    Draws all planets in the solar system.
    """
    x: float = -2050
    for name, size, color in PLANETS:
        x += size * ZOOM + PITCH
        place_planet(name, size, color, x)
        x += size * ZOOM + PITCH


def draw_orbit() -> None:
    """
    Draws an elliptical orbit.
    """
    turtle.penup()
    turtle.goto(77, -70)
    turtle.pendown()
    draw_ellipse(220)


def draw_solar_system() -> None:
    """
    Draws the entire solar system with planets and background stars.
    """
    setup_screen()
    setup_turtle()
    draw_orbit()
    draw_starfield(50)
    draw_planets()
    turtle.done()


# Run the function
draw_solar_system()
