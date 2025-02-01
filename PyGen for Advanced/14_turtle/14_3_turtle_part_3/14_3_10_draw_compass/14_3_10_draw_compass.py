'''
TODO:
    Write a program that draws an image of a compass using a sample.
'''
import turtle


def draw_circle(radius: int) -> None:
    """
    Draws a circle representing the compass.

    Args:
        radius (int): The radius of the circle.

    Returns:
        None: The function draws the circle but does not return any value.
    """
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(0, radius)


def draw_direction(name: str, align: str, font: tuple) -> None:
    """
    Draws a single direction label on the compass.

    Args:
        name (str): The name of the direction (e.g., 'Север', 'Юг').
        align (str): Text alignment ('left', 'center', 'right').
        font (tuple): Font settings for turtle.write().

    Returns:
        None: The function writes the direction on the compass but does not
              return any value.
    """
    turtle.pendown()
    turtle.forward(70)
    turtle.penup()
    turtle.forward(15)
    turtle.write(name, align=align, font=font)
    turtle.goto(0, 20)
    turtle.left(90)


def draw_compass():
    """
    Draws a simple compass using turtle graphics.
    """
    turtle.speed(0)  # Maximum speed
    turtle.penup()

    # Define compass directions
    directions = [
        ('Восток', 'left', ('Arial', 8, 'normal')),
        ('Север', 'center', ('Arial', 8, 'normal')),
        ('Запад', 'right', ('Arial', 8, 'normal')),
        ('Юг', 'center', ('Arial', 8, 'normal'))
    ]

    # Draw compass circle
    draw_circle(20)

    # Draw directions
    for name, align, font in directions:
        draw_direction(name, align, font)

    turtle.done()


# Run the function
draw_compass()
