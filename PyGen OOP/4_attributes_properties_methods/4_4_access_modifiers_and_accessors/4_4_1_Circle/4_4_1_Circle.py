'''
TODO:
    Implement a Circle class that describes a circle.

    When instantiated, the class must accept one argument:
    radius — the radius of the circle

    An instance of the Circle class must have three attributes:
        _radius — the radius of the circle
        _diameter — the diameter of the circle
        _area — the area of the circle

    The Circle class must have three instance methods:
        get_radius() — a method that returns the radius of the circle
        get_diameter() — a method that returns the diameter of the circle
        get_area() — a method that returns the area of the circle

NOTE:
    The area of a circle is calculated using the formula πr ^ 2, where:
        - r — the radius of the circle,
        - π — a constant that expresses the ratio of the circumference to its
        diameter.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from math import pi


class Circle:
    """
    A class representing a circle with radius, diameter, and area.

    This class encapsulates the properties of a circle based on its radius.
    The diameter and area are calculated during initialization and stored
    as private attributes. Methods are provided to access these properties.

    Attributes:
        _radius (float): The radius of the circle.
        _diameter (float): The diameter of the circle (2 * radius).
        _area (float): The area of the circle (π * radius^2).
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize a Circle instance with the given radius.

        Calculates and stores the radius, diameter, and area of the circle
        based on the provided radius.

        Args:
            radius (float): The radius of the circle.

        Returns:
            None
        """
        self._radius: float = radius
        self._diameter: float = radius * 2
        self._area: float = pi * radius * radius

    def get_radius(self) -> float:
        """
        Return the radius of the circle.

        Provides access to the circle's radius.

        Returns:
            float: The radius of the circle.
        """
        return self._radius

    def get_diameter(self) -> float:
        """
        Return the diameter of the circle.

        Provides access to the circle's diameter, calculated as 2 * radius.

        Returns:
            float: The diameter of the circle.
        """
        return self._diameter

    def get_area(self) -> float:
        """
        Return the area of the circle.

        Provides access to the circle's area, calculated as π * radius^2.

        Returns:
            float: The area of the circle.
        """
        return self._area
