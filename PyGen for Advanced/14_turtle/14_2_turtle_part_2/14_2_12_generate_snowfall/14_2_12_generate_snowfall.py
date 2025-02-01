'''
TODO:
    Write a program that randomly draws snowflakes of different colors and
    sizes according to a pattern.
'''
import turtle
import random
import math


def draw_snowflake(size: int, x: int, y: int) -> None:
    """
    Draws a snowflake at a given position with a given size.

    Args:
        size (int): Size of the snowflake.
        x (int): X-coordinate.
        y (int): Y-coordinate.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.colormode(255)  # Enable RGB color mode
    turtle.pencolor(
        random.randint(120, 230),
        random.randint(90, 190),
        random.randint(60, 200)
    )
    turtle.pensize(max(1, size // 15))

    branch = size // 4
    for _ in range(8):
        turtle.forward(size)
        turtle.backward(branch)
        for _ in range(3):
            turtle.left(45)
            turtle.forward(branch)
            turtle.backward(branch)
            turtle.right(90)
            turtle.forward(branch)
            turtle.backward(branch)
            turtle.left(45)
            turtle.backward(branch)
        turtle.left(45)
    turtle.penup()


def is_valid_position(x: int, y: int, size: int, snowflakes: list) -> bool:
    """
    Checks if the given (x, y) position does not overlap significantly with
    existing snowflakes.

    Args:
        x (int): X-coordinate of the new snowflake.
        y (int): Y-coordinate of the new snowflake.
        size (int): Size of the new snowflake.
        snowflakes (list): List of existing snowflakes.

    Returns:
        bool: True if the position is valid, False otherwise.
    """
    for flake in snowflakes:
        distance = math.hypot(x - flake['x'], y - flake['y'])
        min_distance = (size + flake['size']) // 2
        if distance <= min_distance:
            return False
    return True


def generate_snowfall(
    area_size: int = 400,
    min_size: int = 10,
    max_size: int = 50,
    max_attempts: int = 5000
) -> None:
    """
    Generates a snowfall effect with snowflakes randomly placed in the scene.

    Args:
        area_size (int): Half the width/height of the area in which snowflakes
                         are placed.
        min_size (int): Minimum size of a snowflake.
        max_size (int): Maximum size of a snowflake.
        max_attempts (int): Max attempts to find free space for a snowflake.
    """
    screen = turtle.Screen()
    screen.bgcolor('#5CCDC9')

    turtle.speed(0)
    turtle.hideturtle()
    screen.tracer(False)  # Disable screen updates for performance

    snowflakes: list = []
    free_space = area_size * area_size
    attempts = 0

    while free_space > 1000 and attempts < max_attempts:
        x = random.randint(-area_size, area_size)
        y = random.randint(-area_size, area_size)
        size = random.randint(min_size, max_size)

        if is_valid_position(x, y, size, snowflakes):
            draw_snowflake(size, x, y)
            snowflakes.append({'x': x, 'y': y, 'size': size})
            free_space -= size ** 2

        attempts += 1

    screen.update()  # Update screen once all snowflakes are drawn
    turtle.done()


# Run snowfall simulation
generate_snowfall()
