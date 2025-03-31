'''
TODO:
    Implement a Vector class that describes a vector on a plane.

    When instantiating the class, it must accept two arguments in the
    following order:
        - x — the vector's x-coordinate, 0 by default
        - y — the vector's y-coordinate, 0 by default

    An instance of the Vector class must have two attributes:
        - x — the vector's x-coordinate
        - y — the vector's y-coordinate

    The Vector class must have one instance method:
        - abs() — a method that returns the vector's absolute value

NOTE:
    The absolute value of a vector with coordinates (x,y) is calculated using
    the formula:
        sqrt(x^2 + y^2)

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with valid data.
'''
from math import sqrt


class Vector:
    """
    A class representing a 2D vector on a plane.

    This class models a vector with x and y coordinates and provides a method
    to calculate its magnitude (absolute value).

    The coordinates default to 0 if not specified during instantiation.

    Attributes:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.

    Methods:
        abs(): Returns the absolute value (length) of the vector.
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize a Vector instance with x and y coordinates.

        Sets up the vector with the provided or default coordinates.

        Args:
            x (float): The x-coordinate of the vector, defaults to 0.
            y (float): The y-coordinate of the vector, defaults to 0.

        Returns:
            None
        """
        self.x: float = x
        self.y: float = y

    def abs(self) -> float:
        """
        Calculate and return the absolute value of the vector.

        Computes the vector's length using the formula sqrt(x^2 + y^2).

        Returns:
            float: The magnitude (length) of the vector.
        """
        squared_sum = self.x ** 2 + self.y ** 2
        return sqrt(squared_sum)
