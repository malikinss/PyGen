'''
TODO:
    Implement a Point class that describes a point in the plane.

    When instantiated, the class must take two arguments in the following
    order:
        x — the x-coordinate of the point
        y — the y-coordinate of the point

    An instance of the Point class must have the following informal string
    representation:
        (<x-coordinate>, <y-coordinate>)

    Also implement a Circle class that describes a circle in the plane.

    When instantiated, the class must take two arguments in the following
    order:
        radius — the radius of the circle
        center — the point with the coordinates of the center of the circle,
                 represented by an instance of the Point class

    An instance of the Circle class must have the following informal string
    representation:
        (<x-coordinate of the center>, <y-coordinate of the center>),
        r = <radius>

NOTE:
    No additional validation of the data is required.

    It is guaranteed that the implemented classes are used only with valid
    data.

    There are no restrictions regarding class implementations; they can be
    arbitrary.
'''


class Point:
    """
    Point in 2D plane.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Init point.

        Args:
            x: X-coordinate.
            y: Y-coordinate.
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
        Get string representation.

        Returns:
            str: Format (<x>, <y>).
        """
        return f"({self.x}, {self.y})"


class Circle:
    """
    Circle in 2D plane.
    """

    def __init__(self, radius: float, center: Point) -> None:
        """
        Init circle.

        Args:
            radius: Circle radius.
            center: Center point.
        """
        self.r = radius
        self.center = center

    def __str__(self) -> str:
        """
        Get string representation.

        Returns:
            str: Format (<x>, <y>), r = <radius>.
        """
        return f"{self.center}, r = {self.r}"
