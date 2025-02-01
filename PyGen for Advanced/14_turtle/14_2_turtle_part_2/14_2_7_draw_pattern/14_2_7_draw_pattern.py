'''
TODO:
    Write a program that draws a pattern according to a sample.
'''
import turtle


def draw_pattern(
    steps: int, step_increment: int, pen_size_increment: int
) -> None:
    """
    Draws a colorful pattern using turtle graphics.

    Args:
        steps (int): Number of times to repeat the pattern.
        step_increment (int): Value by which step length increases in
                              each iteration.
        pen_size_increment (int): Value by which pen size increases in
                                  each iteration.
    """
    colors = [
        'red', 'blue',
        'yellow', 'green',
        'purple', 'orange'
    ]

    pen_size = 1      # Initial pen size
    step_length = 5   # Initial step length

    for _ in range(steps):
        for color in colors:
            turtle.pensize(pen_size)
            turtle.pencolor(color)
            turtle.forward(step_length)
            turtle.left(45)  # Angle of rotation for the pattern
            step_length += step_increment

        # Increase pen size after each full color cycle
        pen_size += pen_size_increment


# Example usage: 8 iterations, step increases by 3, pen size increases by 2
draw_pattern(8, 3, 2)
