'''
TODO:
    Write a program that draws a crescent moon image using a sample.
'''
import turtle as t


def draw_crescent_moon() -> None:
    """
    Draws a crescent moon using two circles: a larger one for the moon
    and a smaller one for the 'cut-out'.
    """
    # Set up the screen
    t.Screen().setup(380, 480)
    t.Screen().bgcolor(2, 27, 157)  # Night sky color

    # Draw the full moon (larger circle)
    t.penup()
    t.goto(0, -100)  # Position turtle at the center of the moon
    t.pendown()
    t.color(255, 180, 0)  # Moon color (yellow)
    t.begin_fill()
    t.circle(100)  # Draw circle for the moon
    t.end_fill()

    # Draw the 'cut-out' part of the crescent (smaller circle)
    t.penup()
    t.goto(40, -100)  # Move turtle to the position of the cut-out
    t.pendown()
    t.color(2, 27, 157)  # Background color (night sky)
    t.begin_fill()
    t.circle(80)  # Draw smaller circle to create the crescent
    t.end_fill()

    t.hideturtle()


# Run the program
draw_crescent_moon()
