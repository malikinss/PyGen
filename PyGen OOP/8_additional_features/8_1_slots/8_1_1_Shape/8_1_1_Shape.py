'''
TODO:
    Implement a Shape class that describes a geometric shape.

    When instantiated, the class must accept three arguments in the following
    order:
        name — shape name
        color — shape color
        area — shape area

    An instance of the Shape class must have three attributes:
        name — shape name
        color — shape color
        area — shape area

    In addition to the three attributes listed above, an instance of
    the Shape class must not be able to receive any other attributes.

    Also, an instance of the Shape class must have the following informal
    string representation:
        <shape color> <shape name> (<shape area>)

    Finally, instances of the Shape class must support all comparison
    operations between themselves using the ==, !=, >, <, >=, <= operators.

    Two shapes are considered equal if their areas are the same.

    A shape is considered larger than another shape if its area is larger.

NOTE:
    If the object being compared is invalid, the method implementing
    the operation must return the NotImplemented constant.

    There are no restrictions on the implementation of the Shape class,
    it can be arbitrary.
'''
from functools import total_ordering


@total_ordering
class Shape:
    """
    Geometric shape with name, color, and area.
    """
    __slots__ = ("name", "color", "area")

    def __init__(self, name: str, color: str, area: float) -> None:
        """
        Init shape.

        Args:
            name: Shape name.
            color: Shape color.
            area: Shape area.
        """
        self.name = name
        self.color = color
        self.area = area

    def __str__(self) -> str:
        """
        Get string representation.

        Returns:
            str: Format <color> <name> (<area>).
        """
        return f"{self.color} {self.name} ({self.area})"

    def __eq__(self, other: object) -> bool:
        """
        Compare shapes by area.

        Args:
            other: Object to compare.

        Returns:
            bool: True if areas are equal, NotImplemented if invalid.
        """
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area == other.area

    def __lt__(self, other: object) -> bool:
        """
        Compare shapes by area.

        Args:
            other: Object to compare.

        Returns:
            bool: True if area is less, NotImplemented if invalid.
        """
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area < other.area
