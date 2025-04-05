'''
TODO:
    A square trinomial is a polynomial of the form ax^2+bx+c, where a≠0.

    For example:
        x^2 + 1
        x^2 - 5x + 6

    Implement a class QuadraticPolynomial that describes a square trinomial.

    When instantiating the class, it must accept three arguments in
    the following order:
        - a — coefficient a of the square trinomial
        - b — coefficient b of the square trinomial
        - c — coefficient c of the square trinomial

    An instance of the QuadraticPolynomial class must have three attributes:
        - a — coefficient a of the square trinomial
        - b — coefficient b of the square trinomial
        - c — coefficient c of the square trinomial

    The QuadraticPolynomial class must have two class methods:
        - from_iterable() — a method that takes as an argument an iterable
                            object of three elements a, b, and c, which
                            represent the coefficients of the square trinomial,
                            and returns an instance of the QuadraticPolynomial
                            class created based on the passed coefficients
        - from_str() — a method that takes as an argument a string containing
                       the coefficients a, b, and c of the square trinomial,
                       separated by spaces.
                       The method must return an instance of
                       the QuadraticPolynomial class, created based on
                       the passed coefficients, previously converted to
                       instances of the float class

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from collections.abc import Iterable


class QuadraticPolynomial:
    """
    A class representing a square trinomial ax^2 + bx + c.

    Attributes:
        a (float): The coefficient a of the square trinomial.
        b (float): The coefficient b of the square trinomial.
        c (float): The coefficient c of the square trinomial.
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initialize a QuadraticPolynomial instance with coefficients.

        Args:
            a (float): The coefficient a of the square trinomial.
            b (float): The coefficient b of the square trinomial.
            c (float): The coefficient c of the square trinomial.
        """
        self.a: float = a
        self.b: float = b
        self.c: float = c

    @classmethod
    def from_iterable(cls, iterable: Iterable[float]) -> 'QuadraticPolynomial':
        """
        Create a QuadraticPolynomial instance from an iterable of coefficients.

        Args:
            iterable (Iterable[float]): An iterable containing three
                                        coefficients (a, b, c).

        Returns:
            QuadraticPolynomial: A new instance with the given coefficients.
        """
        return cls(*iterable)

    @classmethod
    def from_str(cls, string: str) -> 'QuadraticPolynomial':
        """
        Create a QuadraticPolynomial instance from a string of coefficients.

        Args:
            string (str): A string of three coefficients (a, b, c) separated
                          by spaces.

        Returns:
            QuadraticPolynomial: A new instance with the coefficients
                                 converted to floats.
        """
        a, b, c = map(float, string.split())
        return cls(a, b, c)
