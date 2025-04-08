'''
TODO:
    Implement a Vector class that describes a vector on the plane.

    When instantiating a class, it must accept two arguments in the following
    order:
        x — the vector's x-coordinate
        y — the vector's y-coordinate

    An instance of the Vector class must have the following formal string
    representation:
        Vector(<x-coordinate>, <y-coordinate>)

    Instances of the Vector class must also support comparison operations
    using the == and != operators.

    Two vectors are considered equal if their coordinates on both axes match.

    Methods implementing comparison operations must be able to compare two
    vectors with each other, as well as a vector with a tuple of two numbers
    representing the x- and y-coordinates.

NOTE:
    Instances of the int and float classes will be considered numbers.

    If the object with which the comparison operation is performed is invalid,
    the method implementing this operation must return the NotImplemented
    constant.

    There are no restrictions regarding the implementation of the Vector class;
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

    def __eq__(self, value: object) -> bool:
        """
        Compare the vector with another vector or a tuple for equality.

        Args:
            value (object): The object to compare with (Vector or tuple).

        Returns:
            bool: True if coordinates match, False otherwise.
            NotImplemented: If the comparison is not supported.
        """
        if isinstance(value, Vector):
            return self.x == value.x and self.y == value.y
        if isinstance(value, tuple) and len(value) == 2:
            return self.x == value[0] and self.y == value[1]
        return NotImplemented
