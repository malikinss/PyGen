'''
TODO:
    Write a program that draws a turtle spiral according to the sample.
'''
import turtle


def draw_turtle_spiral(
    initial_step_length: int, step_increment: int, num_steps: int
) -> None:
    """
    Draws a turtle-shaped spiral using the turtle graphics module.

    Args:
        initial_step_length (int): The initial step length for the spiral.
        step_increment (int): The amount by which the step length increases
                              after each iteration.
        num_steps (int): The number of steps to draw in the spiral.
    """
    # Set the screen background color
    turtle.Screen().bgcolor('lawngreen')

    step_length = initial_step_length

    # Move the turtle to the starting position
    turtle.penup()
    turtle.shape('turtle')
    turtle.stamp()  # Stamp a turtle shape at the starting position

    for _ in range(num_steps):
        # Move the turtle forward and make a stamp
        turtle.forward(step_length)
        turtle.right(90)  # Turn the turtle 90 degrees to the right
        turtle.stamp()  # Stamp the turtle shape at the new position
        turtle.left(90)  # Undo the 90 degree turn to keep the path straight
        turtle.backward(step_length)
        turtle.right(20)

        step_length += step_increment


# Example: Draw a spiral with an initial step length of 10, an increment of 3
# and 50 steps
draw_turtle_spiral(10, 3, 50)
