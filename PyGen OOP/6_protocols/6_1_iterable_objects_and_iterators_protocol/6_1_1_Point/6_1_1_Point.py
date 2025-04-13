'''
TODO:
    Implement a Point class that describes a point in space.

    When instantiated, the class must accept three arguments in the following
    order:
        x — the x-coordinate of the point
        y — the y-coordinate of the point
        z — the z-coordinate of the point

    An instance of the Point class must have the following formal string
    representation:
        Point(<x-coordinate>, <y-coordinate>, <z-coordinate>)

    Also, an instance of the Point class must be an iterable object whose
    elements are its x-, y-, and z-coordinates.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Point class,
    it can be arbitrary.
'''
from typing import Any, Iterable


class Point:
    """
    A class representing a point in 3D space with x, y, z coordinates.
    Instances are iterable, yielding their x, y, z coordinates in that order.
    """

    def __init__(self, x: Any, y: Any, z: Any) -> None:
        """
        Initialize a Point with x, y, z coordinates.

        Args:
            x: The x-coordinate of the point.
            y: The y-coordinate of the point.
            z: The z-coordinate of the point.
        """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        """
        Formal string representation of the Point.

        Returns:
            str: String in the format Point(x, y, z).
        """
        return f"Point({self.x}, {self.y}, {self.z})"

    def __iter__(self) -> Iterable[Any]:
        """
        Return an iterator over the point's coordinates.

        Returns:
            Iterable: Iterator yielding x, y, z coordinates in that order.
        """
        return iter((self.x, self.y, self.z))
