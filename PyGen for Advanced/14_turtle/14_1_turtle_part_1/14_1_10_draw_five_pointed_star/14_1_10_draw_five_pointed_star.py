'''
TODO:
    Write a program that draws a regular five-pointed star.

NOTE:
    Use a rotation angle of 144∘.
'''
import turtle


def draw_five_pointed_star(side_length: int) -> None:
    """
    Draws a regular five-pointed star with the given side length using
    Python's Turtle graphics module.

    Args:
        side_length (int): The length of each side of the star.
    """
    for _ in range(5):
        turtle.forward(side_length)  # Draw one side of the star
        turtle.right(144)  # Turn 144 degrees to form the star's points


# Call the function to draw the five-pointed star
draw_five_pointed_star(150)
