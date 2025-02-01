'''
TODO:
    Write a program that draws turtles according to the sample.
'''
import turtle


def draw_turtles_in_circle(num_turtles: int) -> None:
    """
    Draws turtles arranged in a circular pattern.

    Args:
        num_turtles (int): The number of turtles to draw in a circle.
    """
    turtle.penup()  # Lift the pen to avoid drawing lines
    turtle.shape('turtle')  # Set the shape of the turtle
    turtle.stamp()  # Stamp the first turtle at the center

    # Draw the rest of the turtles in a circular pattern
    for _ in range(num_turtles):
        turtle.forward(50)  # Move forward to draw each turtle
        turtle.stamp()  # Stamp a turtle at the current position
        turtle.backward(50)  # Move back to the center
        turtle.left(360 / num_turtles)


# Example: Call the function to draw 8 turtles in a circle
num_turtles = int(input("Enter the number of turtles: "))
draw_turtles_in_circle(num_turtles)
