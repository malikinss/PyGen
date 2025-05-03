'''
TODO:
    Implement a Point data class that describes a point on the coordinate
    plane.

    When instantiated, the class must accept two arguments in the following
    order:
        x — the x-coordinate of the point (type float), defaults to 0.0
        y — the y-coordinate of the point (type float), defaults to 0.0

    An instance of the Point class must have three attributes:
        x — the x-coordinate of the point
        y — the y-coordinate of the point
        quadrant — the coordinate quadrant to which the point belongs (int).

    If the point lies on one of the axes, the quadrant is considered equal to 0

    The Point class must have two instance methods:
        symmetric_x() — a method that returns a new instance of
                        the Point class representing a point symmetrical to
                        the current point about the x-axis
        symmetric_y() — a method that returns a new instance of
                        the Point class representing a point symmetrical to
                        the current point about the y-axis

    An instance of the Point class must have the following formal string
    representation:
        Point(
            x=<x coordinate>, y=<y coordinate>, quadrant=<coordinate quadrant>
        )

    Finally, instances of the Point class must support the comparison
    operation between themselves using the == and != operators.

    Two points are considered equal if their coordinates along both axes
    coincide.

NOTE:
    For a point with coordinates (x, y), we will consider a point with
    coordinates (x, -y) symmetrical about the x-axis, and a point with
    coordinates (-x, y) symmetrical about the y-axis.
'''
from dataclasses import dataclass, field


@dataclass
class Point:
    """
    A data class for a point on the coordinate plane with x, y, and quadrant.
    """
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False, compare=False)

    def __post_init__(self) -> None:
        """
        Compute the quadrant based on x and y coordinates.
        """
        # Map (x_sign, y_sign) to quadrant: 0 for axes, 1-4 for quadrants
        self.quadrant = (
            0 if self.x == 0 or self.y == 0 else
            1 if self.x > 0 and self.y > 0 else
            2 if self.x < 0 and self.y > 0 else
            3 if self.x < 0 and self.y < 0 else 4
        )

    def symmetric_x(self) -> 'Point':
        """
        Return a new Point symmetrical about the x-axis.
        """
        return Point(self.x, -self.y)

    def symmetric_y(self) -> 'Point':
        """
        Return a new Point symmetrical about the y-axis.
        """
        return Point(-self.x, self.y)
