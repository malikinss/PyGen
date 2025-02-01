'''
TODO:
    Write a program that draws an image according to a sample.
'''
import turtle


def draw_pattern(start: int = -200, end: int = 200, step: int = 40) -> None:
    """
    Draws a pattern of blue dots radiating from the center and a red
    central dot.

    Args:
        start (int): The starting position of the dots along the x-axis.
        end (int): The ending position of the dots along the x-axis.
        step (int): The step size between each dot.
    """
    turtle.speed(0)
    turtle.color('green')

    for x in range(start, end, step):
        turtle.goto(x, start)
        turtle.dot(10, 'blue')
        turtle.goto(0, 0)

    # Draw the center red dot
    turtle.color('red')
    turtle.dot(15)


# Example usage
draw_pattern()
