'''
TODO:
        Consider a family of functions — square trinomials.

        All these functions have the same form:
            f(x)=ax^2+bx+c

        Implement the generator_square_polynom() function that takes three
        arguments in the following order:
            a — a real number, coefficient a
            b — a real number, coefficient b
            c — a real number, coefficient c

        The generator_square_polynom() function should return a function that
        takes a real number x as an argument and returns the value of the
        expression ax^2+bx+c.

NOTE:
        Let's consider the example from the first test.

        The call generator_square_polynom(1, 2, 1) returns the function
        corresponding to the square trinomial x^2+2x+1.

        The function is assigned to the variable f.

        The resulting function is then called with the argument 5 and returns
        the value 5^2+5⋅2+1=36.
'''
from typing import Callable


def generator_square_polynom(a: float, b: float, c: float) -> Callable:
    """
    Generates a square polynomial function.

    Args:
        a (float): Coefficient a.
        b (float): Coefficient b.
        c (float): Coefficient c.

    Returns:
        Callable[[float], float]: A function that computes the value of the
        polynomial for a given x.
    """
    return lambda x: (a * x ** 2) + (x * b) + c
