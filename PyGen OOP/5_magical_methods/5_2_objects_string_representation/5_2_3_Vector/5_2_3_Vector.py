'''
TODO:
    Implement a Vector class that describes a vector on the plane.

    When instantiated, the class must accept two arguments in the following
    order:
        - x — the vector's x-coordinate
        - y — the vector's y-coordinate

    An instance of the Vector class must have the following formal string
    representation:
        Vector(<x-coordinate>, <y-coordinate>)

    And the following informal string representation:
        A vector on the plane with coordinates (<x-coordinate>, <y-coordinate>)

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions on the implementation of the Vector class,
    it can be arbitrary.
'''


class Vector:
    """
    A class representing a vector on the plane.
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
            str: The vector in format 'A vector on the plane with coordinates
                 (<x>, <y>)'.
        """
        return f"A vector on the plane with coordinates({self.x}, {self.y})"
