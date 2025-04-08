'''
TODO:
    Implement the ColoredPoint class, which describes a colored point on
    a plane.

    When instantiated, the class must accept three arguments in the following
    order:
        x — the x-coordinate of the point
        y — the y-coordinate of the point
        color — an RGB color represented by a tuple of three integers in
                the range [0; 255], by default it has the value (0, 0, 0)

    An instance of the ColoredPoint class must have three attributes:
        x — the x-coordinate of the point
        y — the y-coordinate of the point
        color — the RGB color, represented as a tuple of three integers from 0
                to 255

    Also, an instance of the ColoredPoint class must have the following formal
    string representation:
        ColoredPoint(
            <x-coordinate>, <y-coordinate>,
            <color of the point as a three-element tuple>
        )

    And the following informal string representation:
        (<x-coordinate>, <y-coordinate>)

    Finally, an instance of the ColoredPoint class must support the unary
    operators +, -, and ~:
        - the result of the unary + must be a new instance of the ColoredPoint
          class with the original coordinates and color
        - the result of the unary - must be a new instance of the ColoredPoint
          class with the coordinates multiplied by minus one, and the original
          color
        - the result of the unary ~ must be a new instance of the ColoredPoint
          class with the coordinates swapped and the color inverted:
            the value of each color component is subtracted from 255

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the ColoredPoint
    class, it can be arbitrary.
'''


from typing import Tuple


class ColoredPoint:
    """
    A class representing a colored point on a plane.
    """

    def __init__(
        self, x: float, y: float, color: Tuple[int, int, int] = (0, 0, 0)
    ) -> None:
        """
        Initialize a ColoredPoint with coordinates and color.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
            color (tuple[int, int, int]): RGB color as a tuple of three
                                          integers (0-255), defaults to
                                          (0, 0, 0).
        """
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self) -> str:
        """
        Formal string representation of the ColoredPoint.

        Returns:
            str: Representation like 'ColoredPoint(1, 2, (255, 0, 0))'.
        """
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"

    def __str__(self) -> str:
        """
        Informal string representation of the ColoredPoint.

        Returns:
            str: Representation like '(1, 2)'.
        """
        return f"({self.x}, {self.y})"

    def __pos__(self) -> 'ColoredPoint':
        """
        Unary + operator: returns a new instance with the same coordinates
        and color.

        Returns:
            ColoredPoint: A new instance with original values.
        """
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self) -> 'ColoredPoint':
        """
        Unary - operator: returns a new instance with negated coordinates.

        Returns:
            ColoredPoint: A new instance with (-x, -y) and original color.
        """
        return ColoredPoint(-self.x, -self.y, self.color)

    def __invert__(self) -> 'ColoredPoint':
        """
        Unary ~ operator: swaps coordinates and inverts color.

        Returns:
            ColoredPoint: A new instance with swapped coordinates and inverted
                          color.
        """
        inverted_color = tuple(255 - component for component in self.color)
        return ColoredPoint(self.y, self.x, inverted_color)
