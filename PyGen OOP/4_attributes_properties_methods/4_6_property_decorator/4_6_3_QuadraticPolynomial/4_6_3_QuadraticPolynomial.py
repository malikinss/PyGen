'''
TODO:
    A square trinomial is a polynomial of the form ax^2+bx+c, where a≠0.

    For example:
        x^2 + 1
        x^2 - 5x + 6

    The value of the variable x at which the square trinomial becomes zero is
    called its root.

    A square trinomial can have one root, two roots, or no roots at all.

    The roots of a square trinomial, if any, are found using the formula:
        x1,2 = (-b ± sqrt(b^2 - 4ac) / 2a

    Implement a class QuadraticPolynomial that describes a square trinomial.

    When instantiated, the class must accept three arguments in the following
    order:
        - a — the coefficient a of the square trinomial
        - b — the coefficient b of the square trinomial
        - c — the coefficient c of the square trinomial

    An instance of the QuadraticPolynomial class must have three attributes:
        - a — the coefficient a of the square trinomial
        - b — the coefficient b of the square trinomial
        - c — the coefficient c of the square trinomial

    The QuadraticPolynomial class must have four properties:
        - x1 — a read-only property that returns the root of the square
        trinomial, calculated using the formula:
            x1 = (-b - sqrt(b^2 - 4ac)) / 2a
        If the square trinomial has no roots:
            (b^2 - 4ac < 0)
        the property value must be None

        - x2 — a read-only property that returns the root of the square
        trinomial calculated by the formula:
            x2 = (-b + sqrt(b^2 - 4ac)) / 2a
        If the square trinomial has no roots:
            (b^2 - 4ac < 0)
        the property value must be None

        - view — a read-only property that returns a string of the form:
            ax^2 + bx + c
        where a, b, and c represent the coefficients of the square trinomial

        - coefficients — a read/write property that returns a tuple of
        the form:
            (a, b, c)
        where a, b, and c represent the coefficients of the square trinomial

NOTE:
    If the square trinomial has only one root, the values of the properties x1
    and x2 must match.

    When changing the coefficients of a square trinomial via the corresponding
    attributes or the coefficients property, the values of the x1, x2, view,
    and coefficients properties must also change.

    If any coefficients of a square trinomial are zero, they must still be
    present in the string returned by the view property, and there is no need
    to remove them.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the QuadraticPolynomial class, it can be arbitrary.
'''
from math import sqrt
from typing import Tuple


class QuadraticPolynomial:
    """
    A class representing a square trinomial ax^2 + bx + c.

    Attributes:
        a (float): The coefficient a of the square trinomial.
        b (float): The coefficient b of the square trinomial.
        c (float): The coefficient c of the square trinomial.

    Properties:
        x1 (float | None): A read-only property returning the first root,
                           or None if no roots exist.
        x2 (float | None): A read-only property returning the second root,
                           or None if no roots exist.
        view (str): A read-only property returning the trinomial as a string:
            'ax^2 + bx + c'.
        coefficients (tuple[float, float, float]): A read-write property
        returning or setting the tuple (a, b, c).
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

    def _calculate_discriminant(self) -> float:
        """Calculate the discriminant of the quadratic polynomial.

        Returns:
            float: The discriminant, calculated as b^2 - 4ac.
        """
        return self.b**2 - 4 * self.a * self.c

    @property
    def x1(self) -> float | None:
        """
        Get the first root of the square trinomial.

        Returns:
            float | None: The root calculated as (-b - sqrt(b^2 - 4ac)) / 2a,
                          or None if no real roots exist (b^2 - 4ac < 0).
        """
        discriminant = self._calculate_discriminant()
        if discriminant < 0:
            return None

        return (-self.b - sqrt(discriminant)) / (2 * self.a)

    @property
    def x2(self) -> float | None:
        """
        Get the second root of the square trinomial.

        Returns:
            float | None: The root calculated as (-b + sqrt(b^2 - 4ac)) / 2a,
                          or None if no real roots exist (b^2 - 4ac < 0).
        """
        discriminant = self._calculate_discriminant()
        if discriminant < 0:
            return None
        return (-self.b + sqrt(discriminant)) / (2 * self.a)

    @property
    def view(self) -> str:
        """
        Get the string representation of the square trinomial.

        Returns:
            str: The trinomial in the form 'ax^2 + bx + c', with proper sign
            handling.
        """
        b_term = f" + {self.b}x" if self.b >= 0 else f" - {abs(self.b)}x"
        c_term = f" + {self.c}" if self.c >= 0 else f" - {abs(self.c)}"
        return f"{self.a}x^2{b_term}{c_term}"

    @property
    def coefficients(self) -> Tuple[float, float, float]:
        """
        Get the coefficients of the square trinomial.

        Returns:
            tuple[float, float, float]: A tuple of coefficients (a, b, c).
        """
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(
        self, coefficients: Tuple[float, float, float]
    ) -> None:
        """
        Set the coefficients of the square trinomial.

        Args:
            coefficients (tuple[float, float, float]): A tuple of new
            coefficients (a, b, c).
        """
        self.a, self.b, self.c = coefficients
