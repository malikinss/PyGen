'''
TODO:
    The equation of a parabola is y = ax^2+bx+c, where a≠0.

    Write a program that, given the input values a, b, c, determines
    and outputs the vertex of the parabola.
'''
from typing import Tuple


def find_parabola_vertex(a: int, b: int, c: int) -> Tuple:
    """
    Calculates the vertex of the parabola given its equation coefficients.

    The equation of a parabola is y = ax^2 + bx + c, where a ≠ 0.
    The vertex (x, y) can be found using the formula:
        x = -b / (2a)
        y = (4ac - b^2) / (4a)

    Args:
        a (int): Coefficient of x^2.
        b (int): Coefficient of x.
        c (int): Constant term.

    Returns:
        Tuple: A tuple containing the coordinates of the vertex (x, y).
    """
    x = (-b) / (2 * a)
    y = (4 * a * c - b * b) / (4 * a)
    return (x, y)


# Input values
a = int(input())
b = int(input())
c = int(input())

# Find and print the vertex
vertex = find_parabola_vertex(a, b, c)
print(vertex)
