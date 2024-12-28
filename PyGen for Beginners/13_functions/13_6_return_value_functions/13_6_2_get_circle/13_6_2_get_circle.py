'''
TODO:
    Write a function get_circle(radius) that takes the radius of a circle
    as an argument and returns two values: the length of the circle
    and the area of the circle bounded by the given circle.
'''
import math


def get_circle(radius: float) -> tuple:
    """
    Calculates the circumference and area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        tuple: A tuple containing the circumference and area of the circle.
               The first value is the circumference, and the second
               is the area.
    """
    # Calculate the circumference and area of the circle
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2

    return circumference, area


# Example usage
r = float(input("Enter the radius of the circle: "))
length, square = get_circle(r)

print(f"Circumference: {length}, Area: {square}")
