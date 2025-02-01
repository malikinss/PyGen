'''
TODO:
    Write a program that draws a STOP sign using the sample.
'''
import turtle


def draw_polygon(sides: int, side_length: float, color: str) -> None:
    """
    Draws a regular polygon.

    Args:
        sides (int): Number of sides in the polygon.
        side_length (float): Length of each side.
        color (str): Fill color of the polygon.
    """
    angle: float = 180 - 180 * (sides - 2) / sides
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(side_length)
        turtle.right(angle)
    turtle.end_fill()


def draw_stop_sign() -> None:
    """
    Draws a STOP sign using an octagon and text.
    """
    turtle.speed(0)

    # Outer black border
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    draw_polygon(8, 100, 'black')

    # White border
    turtle.penup()
    turtle.goto(3, 94)
    turtle.pendown()
    draw_polygon(8, 95, 'white')

    # Red stop sign
    turtle.penup()
    turtle.goto(6, 88)
    turtle.pendown()
    draw_polygon(8, 90, 'red')

    # STOP text
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.write('STOP', font=('Arial', 57, 'bold'), align='center')


# Run the function
draw_stop_sign()
turtle.done()
