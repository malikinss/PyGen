'''
TODO:
    The program is given three lines of text with real numbers, the values of
    the abscissas (x), ordinates (y) and applicates (z) of points in
    three-dimensional space.

    Write a program to check the location of all points with the entered
    coordinates inside or on the surface of a sphere centered at the origin
    and with a radius of R = 2.

NOTE:
    It is guaranteed that the number of numbers in all three lines is the same.

    The equation of the surface of a sphere is x^2 + y^2 + z^2 = R^2

    To solve the problem, use the built-in functions all() and zip().

    Use the following names abscissas, ordinates, applicates for the
    corresponding lists.
'''
from typing import List

RADIUS = 2


def is_inside_sphere(x: float, y: float, z: float) -> bool:
    """
    Checks whether a point is inside or on the surface of a sphere with
    a given radius.

    Args:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
        z (float): The z-coordinate of the point.

    Returns:
        bool: True if the point is inside or on the sphere, False otherwise.
    """
    return x**2 + y**2 + z**2 <= RADIUS**2


def all_points_inside(
    abscissas: List[float], ordinates: List[float], applicates: List[float]
) -> bool:
    """
    Checks whether all given points are inside or on the surface of the sphere.

    Args:
        abscissas (List[float]): A list of x-coordinates.
        ordinates (List[float]): A list of y-coordinates.
        applicates (List[float]): A list of z-coordinates.

    Returns:
        bool: True if all points are inside or on the sphere, False otherwise.
    """
    return all(
        is_inside_sphere(x, y, z)
        for x, y, z in zip(abscissas, ordinates, applicates)
    )


def read_floats() -> List[float]:
    """
    Reads a line of space-separated numbers and converts them to a list
    of floats.

    Returns:
        List[float]: A list of floating-point numbers.
    """
    return list(map(float, input().split()))


abscissas = read_floats()
ordinates = read_floats()
applicates = read_floats()

# Check if all points are inside the sphere and print the result
print(all_points_inside(abscissas, ordinates, applicates))
