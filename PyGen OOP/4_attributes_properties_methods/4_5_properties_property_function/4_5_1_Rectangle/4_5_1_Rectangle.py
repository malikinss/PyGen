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

    The Rectangle class must have two properties:
        - perimeter — a read-only property that returns the perimeter of
                      the rectangle
        - area — a read-only property that returns the area of the rectangle

NOTE:
    When the sides of the rectangle change, its perimeter and area must change.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''


class Rectangle:
    """
    A class representing a rectangle with length and width.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Methods:
        __init__(length, width): Initialize the rectangle with given length
                                 and width.
        get_perimeter(): Calculate and return the perimeter of the rectangle.
        get_area(): Calculate and return the area of the rectangle.

    Properties:
        perimeter (float): A read-only property returning the perimeter,
                          calculated as 2 * (length + width).
        area (float): A read-only property returning the area,
                      calculated as length * width.
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

    def get_perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter, calculated as 2 * (length + width).
        """
        return 2 * (self.length + self.width)

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area, calculated as length * width.
        """
        return self.length * self.width

    perimeter = property(fget=get_perimeter)
    area = property(fget=get_area)
