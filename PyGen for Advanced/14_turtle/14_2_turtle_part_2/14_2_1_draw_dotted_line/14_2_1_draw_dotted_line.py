'''
TODO:
    Write a program that draws a dotted line

NOTE:
    Experiment with the shape of the turtle.
'''
import turtle


def draw_dotted_line(dot_distance: int, num_dots: int, dot_size: int) -> None:
    """
    Draws a dotted line by moving the turtle forward and placing dots
    at regular intervals.

    Args:
        dot_distance (int): Distance between each dot.
        num_dots (int): Number of dots to draw.
        dot_size (int): The size of each dot.
    """
    turtle.penup()  # Lift the pen to move without drawing
    turtle.backward(100)  # Start a little left to center the line

    for _ in range(num_dots):
        turtle.forward(dot_distance)  # Move forward by the distance
        turtle.dot(dot_size)          # Draw a dot with the given size


# Call the function to draw a dotted line
draw_dotted_line(dot_distance=20, num_dots=10, dot_size=10)
