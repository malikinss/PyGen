'''
TODO:
    Implement a Circle class that describes a circle.

    When instantiated, the class must accept one argument:
        - radius — the radius of the circle

    An instance of the Circle class must have one attribute:
        - radius — the radius of the circle

    The Circle class must have one class method:
        - from_diameter() — a method that takes the diameter of the circle as
        an argument and returns an instance of the Circle class created based
        on the passed diameter

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''


class Circle:
    """
    A class representing a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize a Circle instance with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius: float = radius

    @classmethod
    def from_diameter(cls, diameter: float) -> 'Circle':
        """
        Create a Circle instance from a given diameter.

        Args:
            diameter (float): The diameter of the circle.

        Returns:
            Circle: A new Circle instance with radius calculated as:
                        diameter / 2
        """
        return cls(diameter / 2)
