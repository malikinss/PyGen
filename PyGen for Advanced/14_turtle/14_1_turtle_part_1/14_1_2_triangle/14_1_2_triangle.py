'''
TODO:
    Write a program that draws a regular triangle.

NOTE:
    The program should be written as a function triangle(side), where side is
    the length of the triangle's side in pixels.

    The size of each angle of a regular triangle is 60 degrees.
'''
import turtle


def triangle(side: int) -> None:
    """
    Draws an equilateral triangle with the given side length using Python's
    Turtle graphics module.

    Args:
        side (int): the length of the side of the triangle.
    """
    for _ in range(3):
        turtle.forward(side)  # Draw one side of the triangle
        turtle.left(120)       # Turn 120 degrees to form the triangle's angles


side = int(input("Enter the side length of the triangle: "))

triangle(side)
