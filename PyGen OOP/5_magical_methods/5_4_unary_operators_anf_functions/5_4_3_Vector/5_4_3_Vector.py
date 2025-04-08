'''
TODO:
    Implement a Vector class that describes a vector in the plane.

    When instantiated, the class must accept two arguments in the following
    order:
        x — the vector's x-coordinate
        y — the vector's y-coordinate

    An instance of the Vector class must have the following formal string
    representation:
        Vector(<x-coordinate>, <y-coordinate>)

    And the following informal string representation:
        (<vector's x-coordinate>, <vector's y-coordinate>)

    Also, an instance of the Vector class must support the unary
    operators + and -:
        - the result of the unary + must be a new instance of the Vector class
          with the original coordinates
        - the result of the unary - must be a new instance of the Vector class
          with the coordinates taken with the opposite sign

    Finally, when passing an instance of the Vector class to the abs()
    function, its modulus must be returned.

NOTE:
    The modulus of a vector with coordinates (x,y) is calculated using
    the formula sqrt(x^2 + y^2)

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Vector class,
    it can be arbitrary.
'''
from math import sqrt


class Vector:
    """
    A class representing a vector in the plane with x and y coordinates.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initialize a Vector instance.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """
        Return a formal string representation of the vector.

        Returns:
            str: The vector in format 'Vector(<x>, <y>)'.
        """
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        """
        Return an informal string representation of the vector.

        Returns:
            str: The vector in format '(<x>, <y>)'.
        """
        return f"({self.x}, {self.y})"

    def __pos__(self) -> 'Vector':
        """
        Return a new Vector instance with the same coordinates.

        Returns:
            Vector: A new instance with original coordinates.
        """
        return Vector(self.x, self.y)

    def __neg__(self) -> 'Vector':
        """
        Return a new Vector instance with negated coordinates.

        Returns:
            Vector: A new instance with coordinates (-x, -y).
        """
        return Vector(-self.x, -self.y)

    def __abs__(self) -> float:
        """
        Return the modulus of the vector.

        Returns:
            float: The modulus calculated as sqrt(x^2 + y^2).
        """
        return sqrt(self.x ** 2 + self.y ** 2)
