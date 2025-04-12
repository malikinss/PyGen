'''
TODO:
    Implement the ColoredPoint class that describes a colored point on a plane.

    When instantiated, the class must accept three arguments in the following
    order:
        x — the x-coordinate of the point
        y — the y-coordinate of the point
        color — the color of the point

    The ColoredPoint class must have three properties:
        x — a read-only property that returns the x-coordinate of the point
        y — a read-only property that returns the y-coordinate of the point
        color — a read-only property that returns the color of the point

    An instance of the ColoredPoint class must have the following formal
    string representation:
        ColoredPoint(<x-coordinate>, <y-coordinate>, '<color of the point>')

    Also, instances of the ColoredPoint class must support comparison
    operations with each other using the == and != operators.

    Two colored points are considered equal if their colors and coordinates
    along both axes match.

    Finally, when passing an instance of the ColoredPoint class to
    the hash() function, its hash value must be returned, calculated using
    the hash() function based on a tuple whose first element is
    the x-coordinate of the point, the second is the y-coordinate of the point,
    and the third is the color of the point.

NOTE:
    If the object being compared is invalid, the method implementing
    the comparison operation must return the NotImplemented constant.

    There are no restrictions regarding the implementation of
    the ColoredPoint class, it can be arbitrary.
'''
from typing import Any


class ColoredPoint:
    """
    A class representing a colored point on a plane with x, y coordinates
    and color.

    Attributes:
        x: The x-coordinate of the point (read-only).
        y: The y-coordinate of the point (read-only).
        color: The color of the point (read-only).
    """

    def __init__(self, x: Any, y: Any, color: Any) -> None:
        """
        Initialize a ColoredPoint with coordinates and color.

        Args:
            x: The x-coordinate of the point.
            y: The y-coordinate of the point.
            color: The color of the point.
        """
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self) -> Any:
        """
        The x-coordinate of the point.

        Returns:
            The x-coordinate value.
        """
        return self._x

    @property
    def y(self) -> Any:
        """
        The y-coordinate of the point.

        Returns:
            The y-coordinate value.
        """
        return self._y

    @property
    def color(self) -> Any:
        """
        The color of the point.

        Returns:
            The color value.
        """
        return self._color

    def __repr__(self) -> str:
        """
        Formal string representation of the ColoredPoint.

        Returns:
            str: String in the format ColoredPoint(x, y, 'color').
        """
        return f"ColoredPoint({self._x}, {self._y}, '{self._color}')"

    def __eq__(self, other: Any) -> bool:
        """
        Check equality with another object.

        Args:
            other: Object to compare with.

        Returns:
            bool: True if other is a ColoredPoint with equal x, y, and color;
                  False otherwise.
            NotImplemented if other is not a valid ColoredPoint.
        """
        if not isinstance(other, ColoredPoint):
            return NotImplemented
        return (self._x == other._x and
                self._y == other._y and
                self._color == other._color)

    def __hash__(self) -> int:
        """
        Compute hash value based on coordinates and color.

        Returns:
            int: Hash of the tuple (x, y, color).
        """
        return hash((self._x, self._y, self._color))
