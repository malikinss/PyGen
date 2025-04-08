'''
TODO:
    Implement a Vector class that describes a vector on a plane.

    When creating an instance, the class must accept two arguments in the
    following order:
        x — the vector's x-coordinate
        y — the vector's y-coordinate

    An instance of the Vector class must have the following formal string
    representation:
        Vector(<x-coordinate>, <y-coordinate>)

    Also, instances of the Vector class must support the operations of
    addition and subtraction between themselves using the + and - operators,
    respectively:
        - the result of addition must be a new instance of the Vector class,
          the x-coordinate of which is equal to the sum of the x-coordinates
          of the original vectors, and the y-coordinate of which is equal to
          the sum of the y-coordinates of the original vectors
        - the result of subtraction must be a new instance of the Vector class,
          the x-coordinate of which is equal to the difference of
          the x-coordinates of the original vectors, taking into account
          the order, and the y-coordinate of which is the difference of
          the y-coordinates of the original vectors, taking into account
          the order

    Finally, an instance of the Vector class must support the operations of
    multiplication and division by a number n using the * and / operators,
    respectively:
        - the result of multiplication must be a new instance class Vector,
          whose coordinates are multiplied by n
        - the result of division should be a new instance of class Vector,
          whose coordinates are divided by n

    The multiplication operation should be feasible regardless of the order of
    the operands, i.e. it should be possible to multiply both a vector by
    a number and a number by a vector.

NOTE:
    We will consider instances of classes int and float as numbers.

    We will also guarantee that an instance of class Vector is always divided
    by a non-zero number.

    If the object with which the arithmetic operation is performed is
    incorrect, the method implementing this operation should return
    the NotImplemented constant.

    There are no restrictions regarding the implementation of the Vector class,
    it can be arbitrary.
'''
from typing import Union


class Vector:
    """
    A class representing a vector on a plane.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initialize Vector with x and y coordinates.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """
        Formal string representation of the Vector.

        Returns:
            str: Representation like 'Vector(1, 2)'.
        """
        return f"Vector({self.x}, {self.y})"

    def __add__(
        self, other: 'Vector'
    ) -> 'Union[Vector, NotImplemented]':  # type:ignore
        """
        Add two Vector instances.

        Args:
            other (Vector): Another Vector instance to add.

        Returns:
            Vector: New instance with summed coordinates.
            NotImplemented: If other is not a Vector instance.
        """
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
        return NotImplemented

    def __sub__(
        self, other: 'Vector'
    ) -> 'Union[Vector, NotImplemented]':  # type:ignore
        """
        Subtract another Vector from this one.

        Args:
            other (Vector): Another Vector instance to subtract.

        Returns:
            Vector: New instance with subtracted coordinates.
            NotImplemented: If other is not a Vector instance.
        """
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
            return Vector(x, y)
        return NotImplemented

    def __mul__(
        self, n: Union[int, float]
    ) -> 'Union[Vector, NotImplemented]':  # type:ignore
        """Multiply Vector by a scalar.

        Args:
            n (int | float): Scalar to multiply by.

        Returns:
            Vector: New instance with scaled coordinates.
            NotImplemented: If n is not a number.
        """
        if isinstance(n, (int, float)):
            x = self.x * n
            y = self.y * n
            return Vector(x, y)
        return NotImplemented

    def __rmul__(
        self, n: Union[int, float]
    ) -> 'Union[Vector, NotImplemented]':  # type:ignore
        """
        Right multiply Vector by a scalar (n * Vector).

        Args:
            n (int | float): Scalar to multiply by.

        Returns:
            Vector: New instance with scaled coordinates.
            NotImplemented: If n is not a number.
        """
        return self.__mul__(n)

    def __truediv__(
        self, n: Union[int, float]
    ) -> 'Union[Vector, NotImplemented]':  # type:ignore
        """
        Divide Vector by a scalar.

        Args:
            n (int | float): Scalar to divide by.

        Returns:
            Vector: New instance with divided coordinates.
            NotImplemented: If n is not a number.
        """
        if isinstance(n, (int, float)):
            x = self.x / n
            y = self.y / n
            return Vector(x, y)
        return NotImplemented
