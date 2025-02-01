'''
TODO:
    Write a program that draws a rainbow image using a sample.
'''
import turtle


def draw_rainbow_arc(radius: int, color: str, y_offset: int) -> None:
    """
    Draws a single arc of the rainbow.

    Args:
        radius (int): The radius of the arc.
        color (str): The color of the arc.
        y_offset (int): The vertical offset for the current arc.
    """
    turtle.fillcolor(color)
    turtle.penup()
    turtle.goto(0, y_offset)  # Position the turtle to the correct height
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius, 180)  # Draw a half-circle (arc)
    turtle.end_fill()


def draw_rainbow() -> None:
    """
    Draws the entire rainbow with multiple colored arcs.
    """
    turtle.speed(0)
    turtle.hideturtle()

    # Define rainbow colors and initial radius
    colors = [
        'red', 'orange', 'yellow', 'chartreuse', 'light green',
        'cyan', 'dodgerblue', 'blue', 'magenta', 'hotpink'
    ]
    radius = 100
    y_offset = 0

    # Draw each arc of the rainbow
    for color in colors:
        draw_rainbow_arc(radius, color, y_offset)
        radius -= 10  # Decrease the radius for each subsequent arc
        y_offset += 10  # Increase the vertical offset for each subsequent arc


# Run the program
draw_rainbow()
