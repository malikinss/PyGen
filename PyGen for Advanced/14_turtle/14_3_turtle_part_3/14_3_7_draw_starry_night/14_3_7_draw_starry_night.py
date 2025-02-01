'''
TODO:
    Write a program that draws an image based on a sample.

    The stars should be randomly scattered, of different sizes and colors.
'''
import turtle as t
from random import randint, randrange


def setup_turtle_screen() -> None:
    """
    Sets up the turtle screen and its settings like tracer, color mode,
    and background color.
    """
    t.tracer(1, 0)
    t.colormode(255)
    t.bgcolor('black')


def generate_random_position() -> tuple[int, int]:
    """
    Generates a random position for the star on the screen.

    Returns:
        tuple[int, int]: Random x and y coordinates for the star.
    """
    x = randint(-300, 300)
    y = randint(-300, 300)
    return x, y


def generate_random_color() -> tuple[int, int, int]:
    """
    Generates a random RGB color for the star.

    Returns:
        tuple[int, int, int]: Random RGB values for the star's color.
    """
    res: tuple = tuple(randint(0, 255) for _ in range(3))
    return res


def draw_star(size: int) -> None:
    """
    Draws a star with the given size.

    Args:
        size (int): The size of the star.
    """
    for _ in range(5):
        t.forward(size)
        t.right(144)


def move_to_random_position() -> None:
    """
    Moves the turtle to a random position on the screen.
    """
    x, y = generate_random_position()  # Get random position
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_random_star() -> None:
    """
    Draws a random star with random size, position, and color on the screen.
    """
    # Set random orientation and speed
    t.setheading(randrange(0, 360))
    t.speed(randrange(1, 11))

    # Move to random position
    move_to_random_position()

    # Set a random color for the star
    t.fillcolor(generate_random_color())

    # Draw the star
    t.begin_fill()
    draw_star(randint(2, 50))  # Using the draw_star function here
    t.end_fill()


def draw_starry_night() -> None:
    """
    Sets up the screen, draws 200 stars, and finishes the drawing.
    """
    setup_turtle_screen()

    # Draw 200 stars
    for _ in range(200):
        draw_random_star()

    # End the drawing
    t.done()


# Call the function to execute the program
draw_starry_night()
