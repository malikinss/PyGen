'''
TODO:
    Implement a Circle class that describes a circle.

    When instantiated, the class must accept one argument:
        - radius — the radius of the circle

    An instance of the Circle class must have three attributes:
        - radius — the radius of the circle
        - diameter — the diameter of the circle
        - area — the area of the circle

NOTE:
    The area of a circle is calculated using the formula πr ^ 2, where r is
    the radius of the circle, π is a constant that expresses the ratio of the
    circumference to its diameter.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from math import pi


class Circle:
    """
    A class representing a circle.

    Attributes:
        radius (float): The radius of the circle.
        diameter (float): The diameter of the circle, calculated as 2 * radius.
        area (float): The area of the circle, calculated as π * radius^2.

    Methods:
        __init__(radius: float) -> None:
            Initializes a new Circle instance with the given radius.
    """

    def __init__(self, radius: float) -> None:
        """
        Initializes a new Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius
        self.diameter = self.radius * 2
        self.area = pi * (self.radius ** 2)
