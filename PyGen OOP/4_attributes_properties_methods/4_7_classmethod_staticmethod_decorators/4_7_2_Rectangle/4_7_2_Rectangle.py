'''
TODO:
    Implement a Rectangle class that describes a rectangle.

    When instantiated, the class must accept two arguments in the following
    order:
        - length — the length of the rectangle
        - width — the width of the rectangle

    An instance of the Rectangle class must have two attributes:
        - length — the length of the rectangle
        - width — the width of the rectangle

    The Rectangle class must have one class method:
        - square() — a method that accepts a side number as an argument and
                     returns an instance of the Rectangle class with a length
                     and width equal to side

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    """

    def __init__(self, length: float, width: float) -> None:
        """
        Initialize a Rectangle instance with length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length: float = length
        self.width: float = width

    @classmethod
    def square(cls, side: float) -> 'Rectangle':
        """
        Create a Rectangle instance representing a square.

        Args:
            side (float): The length of the square's side.

        Returns:
            Rectangle: A new Rectangle instance with length and width equal
                       to side.
        """
        return cls(side, side)
