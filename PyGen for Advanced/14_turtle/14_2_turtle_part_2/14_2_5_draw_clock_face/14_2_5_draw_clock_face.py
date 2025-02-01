'''
TODO:
    Write a program that draws a clock face according to the sample.
'''
import turtle as t


def draw_clock_face(num_marks: int) -> None:
    """
    Draws a clock face with a given number of marks (ticks) around the edge.

    Args:
        num_marks (int): The number of hour marks (ticks) to draw on the clock
                         face.
    """
    t.penup()  # Lift the pen to start drawing without lines
    t.pensize(3)  # Set the pen size to make the ticks visible
    t.shape('turtle')  # Use a turtle shape for stamping

    for i in range(num_marks):
        t.forward(70)  # Move to the position where the tick will be drawn
        t.pendown()  # Lower the pen to draw the tick
        t.forward(15)  # Draw the tick
        t.penup()  # Lift the pen again
        t.forward(15)  # Move to the next position
        t.stamp()  # Stamp a turtle to mark the position
        t.backward(100)  # Move back to the center of the clock
        t.left(360 / num_marks)  # Rotate for the next tick position

    t.stamp()  # Stamp at the center of the clock


# Example: Call the function to draw a clock face with 12 ticks (for hours)
num_marks = int(input("Enter the number of marks for the clock face: "))
draw_clock_face(num_marks)
