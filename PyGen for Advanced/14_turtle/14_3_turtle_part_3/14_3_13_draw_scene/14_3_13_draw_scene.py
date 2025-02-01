'''
TODO:
    Write a program that draws silhouettes of multi-story buildings using
    a template.

    Divide the program into functions:
        - Drawing the outlines of buildings;
        - Drawing several windows in buildings;
        - Drawing randomly scattered stars as dots (make sure the stars appear
          in the sky, not on the buildings).
'''

import turtle
from random import choice as c, randrange as r
from typing import Tuple, List

# Type aliases
Color = Tuple[int, int, int]


def setup_screen(bg_color: Color):
    """
    Configures the turtle screen.

    Args:
        bg_color (Color): Background color for the sky.

    """
    screen = turtle.Screen()
    screen.setup(660, 660)
    # screen.colormode(255)  # Uncomment if using a local interpreter
    screen.bgcolor(bg_color)


def create_turtle(
    color: Color, speed: int = 0, hide: bool = True
) -> turtle.Turtle:
    """
    Creates and configures a turtle.

    Args:
        color (Color): The color of the turtle.
        speed (int, optional): The speed of drawing. Defaults to 0 (fastest).
        hide (bool, optional): Whether to hide the turtle cursor.
                               Defaults to True.

    Returns:
        turtle.Turtle: Configured turtle instance.
    """
    t = turtle.Turtle()
    t.speed(speed)
    t.color(color)
    t.fillcolor(color)
    t.penup()
    if hide:
        t.hideturtle()
    return t


def draw_stars(
    t: turtle.Turtle,
    star_color: Color,
    num_stars: int,
    star_sizes: Tuple[int, ...]
) -> None:
    """
    Draws randomly scattered stars in the sky.

    Args:
        t (turtle.Turtle): The turtle used for drawing.
        star_color (Color): The color of the stars.
        num_stars (int): Number of stars to draw.
        star_sizes (Tuple[int, ...]): Possible sizes of the stars.
    """
    t.color(star_color)
    for _ in range(num_stars):
        t.setposition(r(-325, 326), r(-100, 326))  # Only in the sky area
        t.dot(c(star_sizes))


def draw_windows(
    t: turtle.Turtle,
    wx: int,
    wy: int,
    window_size: int,
    probability: int
) -> None:
    """
    Draws windows on a building.

    Args:
        t (turtle.Turtle): The turtle used for drawing windows.
        wx (int): The x-coordinate of the building.
        wy (int): The y-coordinate of the building.
        window_size (int): The size of the windows.
        probability (int): The probability of drawing a window (0-100).
    """
    while wy > -300:  # Stop at the bottom of the screen
        if r(101) >= 100 - probability:  # Probability-based window drawing
            t.begin_fill()

            # Random left/right offset
            t.setposition(wx + 5 + c((0, 30)), wy - 5)
            for _ in range(4):
                t.forward(window_size)
                t.right(90)
            t.end_fill()
        wy -= 30  # Move to the next floor down


def draw_buildings(
    t: turtle.Turtle,
    wt: turtle.Turtle,
    building_color: Color,
    build_borders: List[Tuple[int, int]],
    window_size: int,
    probability: int
) -> None:
    """
    Draws the silhouette of multiple buildings.

    Args:
        t (turtle.Turtle): The turtle used for drawing buildings.
        wt (turtle.Turtle): The turtle used for drawing windows.
        building_color (Color): The color of the buildings.
        build_borders (List[Tuple[int, int]]): Coordinates of the building
                                               boundaries.
        window_size (int): The size of the windows.
        probability (int): The probability of drawing a window.
    """
    t.color(building_color)
    t.fillcolor(building_color)

    # Start from the left boundary
    x, y = build_borders[-1]
    ox, oy = 0, 0  # Previous x, y values for avoiding duplicate walls
    t.penup()
    t.setposition(x, y)
    t.pendown()

    t.begin_fill()
    while x < 330:  # Stop at the right boundary
        dx = c((0, 0, 0, 60))  # Random step: 0 (vertical wall) or 60 (roof)
        if not dx:  # Vertical wall
            dy = c((-60, 60))  # Random height change
            if -100 <= y + dy <= 200 and ((y + dy) != oy or x != ox):
                ox, oy = x, y  # Store previous values
                y += dy  # Adjust height
        else:  # Roof
            # Draw windows only when moving horizontally
            draw_windows(wt, x, y, window_size, probability)
            x += dx  # Adjust width
        t.setposition(x, y)  # Move turtle

    # Fill buildings using pre-defined bottom boundary
    for point in build_borders:
        t.setposition(point)
    t.end_fill()


def draw_scene() -> None:
    """
    Main function to initialize the scene and draw stars, buildings,
    and windows.
    """
    # Define colors
    sky_color: Color = (0, 30, 66)
    building_color: Color = (2, 67, 160)
    window_color: Color = (255, 252, 138)

    # Define other constants
    star_sizes: Tuple[int, int, int, int] = (4, 4, 4, 9)
    num_stars: int = 30
    window_size: int = 20
    window_probability: int = 10
    building_borders: List = [(330, -330), (-330, -330), (-330, -100)]

    # Set up the screen
    setup_screen(sky_color)

    # Create turtles
    star_turtle = create_turtle(window_color)
    building_turtle = create_turtle(building_color, speed=0, hide=False)
    window_turtle = create_turtle(window_color)

    # Draw elements
    draw_stars(star_turtle, window_color, num_stars, star_sizes)
    draw_buildings(
        building_turtle,
        window_turtle,
        building_color,
        building_borders,
        window_size,
        window_probability
    )

    # Keep the window open
    turtle.done()


draw_scene()
