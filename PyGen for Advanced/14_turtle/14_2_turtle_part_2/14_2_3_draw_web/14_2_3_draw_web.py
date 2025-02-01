'''
TODO:
    Write a program to draw a web according to the example.

    The program should read the number of rays of the web, the number n.

NOTE:
    The angle given by each pair of rays is 360/n degrees.
'''
import turtle


def draw_web(num_rays: int, radius: int = 100) -> None:
    """
    Draws a web with the given number of rays and radius.

    Args:
        num_rays (int): The number of rays in the web.
        radius (int, optional): The radius of the rays. Default is 100.
    """
    # Loop to draw each ray of the web
    for _ in range(num_rays):
        turtle.forward(radius)  # Move forward to draw a ray
        turtle.stamp()           # Place a stamp (dot) at the end of the ray
        turtle.backward(radius)  # Move backward to the center
        turtle.left(360 / num_rays)  # Rotate to draw the next ray

    turtle.dot(20)  # Place a central dot to represent the center of the web


# Input for the number of rays
num_rays = int(input("Enter the number of rays: "))

# Call the function to draw the web
draw_web(num_rays)
