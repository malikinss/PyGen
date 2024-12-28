'''
TODO:
    Write a function solve(a, b, c) that takes as arguments three integers
    a, b, c - the coefficients of the quadratic equation ax^2+bx+c=0
    and returns its roots in ascending order.
'''
import math


def solve(a: int, b: int, c: int) -> tuple:
    """
    Solves the quadratic equation ax^2 + bx + c = 0.

    Args:
        a (int): The coefficient of x^2.
        b (int): The coefficient of x.
        c (int): The constant term.

    Returns:
        tuple: A tuple containing the roots of the quadratic equation
               in ascending order.
               If no real roots exist, returns a message indicating so.
    """
    D = b ** 2 - 4 * a * c  # Discriminant

    # Calculate the roots
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)

    return min(x1, x2), max(x1, x2)


# Example usage
a, b, c = int(input()), int(input()), int(input())
result = solve(a, b, c)

if isinstance(result, tuple):
    print(result[0], result[1])
else:
    print(result)  # If no real roots, print the message
