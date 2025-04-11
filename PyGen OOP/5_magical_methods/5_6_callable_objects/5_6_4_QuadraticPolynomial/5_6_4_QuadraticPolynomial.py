'''
TODO:
    Implement a QuadraticPolynomial class that describes a square trinomial.

    When instantiated, the class must accept three arguments in the following
    order:
        a — coefficient a of the square trinomial
        b — coefficient b of the square trinomial
        c — coefficient c of the square trinomial

    An instance of the QuadraticPolynomial class must be a callable object and
    accept one argument:
        x — number

    An instance of the QuadraticPolynomial class must return the value of
    the expression ax^2+bx+c, where a,b, and c are the coefficients of
    the square trinomial.

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with valid data.

    There are no restrictions on the implementation of the QuadraticPolynomial
    class, it can be arbitrary.
'''
from typing import Union


class QuadraticPolynomial:
    """
    A class representing a quadratic polynomial (ax^2 + bx + c).
    """

    def __init__(
        self, a: Union[int, float], b: Union[int, float], c: Union[int, float]
    ) -> None:
        """
        Initialize QuadraticPolynomial with coefficients a, b, and c.

        Args:
            a (int | float): Coefficient of x^2.
            b (int | float): Coefficient of x.
            c (int | float): Constant term.
        """
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x: Union[int, float]) -> Union[int, float]:
        """
        Evaluate the quadratic polynomial for a given x.

        Args:
            x (int | float): The value to evaluate the polynomial at.

        Returns:
            int | float: The result of ax^2 + bx + c.
        """
        return self.a * x**2 + self.b * x + self.c
