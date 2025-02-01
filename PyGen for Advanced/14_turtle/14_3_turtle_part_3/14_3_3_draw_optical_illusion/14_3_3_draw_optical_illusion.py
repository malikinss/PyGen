'''
TODO:
    Write a program that draws an optical illusion from a sample.
'''
import turtle


def draw_triangle(side_length: int, color: str) -> None:
    """
    Draws an equilateral triangle with the given side length and color.

    Args:
        side_length (int): The length of the sides of the triangle.
        color (str): The color of the triangle.
    """
    turtle.color(color)
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)


def draw_optical_illusion() -> None:
    """
    Draws the optical illusion consisting of triangles and dots.
    """
    turtle.speed(5)

    # Draw the outer triangle
    draw_triangle(90, 'black')

    # Move to the position for the inner shape
    turtle.penup()
    turtle.goto(0, 60)

    # Draw the inner shape with white triangles and black dots
    turtle.color('white')
    turtle.fillcolor('white')
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(90)
        turtle.color('black')
        turtle.dot(30)
        turtle.color('white')
        turtle.right(120)

    turtle.end_fill()


# Run the program
draw_optical_illusion()
