'''
TODO:
    Implement a Vector class that describes a vector on a plane.

    When instantiating a class, it must accept two arguments in the following
    order:
        x — the vector's x-coordinate
        y — the vector's y-coordinate

    An instance of the Vector class must have the following informal string
    representation:
        (<x-coordinate>, <y-coordinate>)

    An instance of the Vector class must also support casting to bool, int,
    float, and complex types:
        - when casting to bool, the vector's value must be True if at least
          one of its coordinates is nonzero, or False otherwise
        - when casting to int, the vector's value must be its absolute value
          as an integer with the fractional part discarded
        - when casting to float, the vector's value must be its absolute value
          as a real number
        - when casting to complex, the vector's value must be a complex number
          whose real part is equal to the vector's x-coordinate and whose
          imaginary part is equal to the vector's y-coordinate

NOTE:
    The absolute value of a vector with coordinates (x,y) is calculated using
    the formula:
        sqrt(x**2 + y**2)

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Vector class,
    it can be arbitrary.
'''
from math import sqrt
from typing import Union


class Vector:
    """
    A class representing a vector on a plane with x and y coordinates.
    """

    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        """
        Initialize Vector with x and y coordinates.

        Args:
            x (int | float): The x-coordinate of the vector.
            y (int | float): The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
        Return informal string representation of the vector.

        Returns:
            str: String in the format '(<x>, <y>)'.
        """
        return f'({self.x}, {self.y})'

    def __bool__(self) -> bool:
        """
        Return True if at least one coordinate is nonzero, False otherwise.

        Returns:
            bool: True if x or y is nonzero, False if both are zero.
        """
        return bool(self.x or self.y)

    def __abs__(self) -> float:
        """
        Return the absolute value (magnitude) of the vector.

        Returns:
            float: The square root of (x^2 + y^2).
        """
        return sqrt(self.x**2 + self.y**2)

    def __int__(self) -> int:
        """
        Return the integer absolute value of the vector.

        Returns:
            int: The absolute value with the fractional part discarded.
        """
        return int(abs(self))

    def __float__(self) -> float:
        """
        Return the floating-point absolute value of the vector.

        Returns:
            float: The absolute value as a real number.
        """
        return abs(self)

    def __complex__(self) -> complex:
        """
        Return the vector as a complex number (x + yj).

        Returns:
            complex: Complex number with x as real part and y as imaginary
            part.
        """
        return complex(self.x, self.y)
