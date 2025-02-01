'''
TODO:
    Write a program that draws an image of a traffic light using a sample.
'''
import turtle as t


def draw_rectangle(width: int, height: int, x: int, y: int):
    """
    Draws a filled rectangle with the given width, height, and
    starting position.

    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the starting point.
        y (int): Y-coordinate of the starting point.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()


def draw_traffic_light():
    """
    Draws a traffic light with three colored circles (red, yellow, and green)
    inside a black rectangular body.
    """
    t.hideturtle()

    # Draw the traffic light body (a black rectangle)
    t.fillcolor('black')
    draw_rectangle(120, 300, -60, 150)

    # Colors for the lights (red, yellow, green)
    colors = ['red', 'yellow', 'lime']

    # Draw the colored lights
    for i, color in enumerate(colors):
        t.penup()
        t.goto(0, 90 - i * 90)  # Adjust the position for each light
        t.pendown()
        t.dot(80, color)  # Draw the light circle


# Run the drawing function
draw_traffic_light()
