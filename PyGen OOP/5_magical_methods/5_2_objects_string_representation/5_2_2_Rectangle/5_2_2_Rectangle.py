'''
TODO:
    You have access to the Rectangle class, which describes a rectangle.

    When instantiated, the class takes two arguments in the following order:
        - length — the length of the rectangle
        - width — the width of the rectangle

    Implement the following formal and informal string representation for
    instances of the Rectangle class:
        Rectangle(<length of the rectangle>, <width of the rectangle>)

NOTE:
    No additional validation of the data is required.

    It is guaranteed that the implemented class is used only with valid data.

    There are no restrictions regarding the implementation of the Rectangle
    class, it can be arbitrary.
'''


class Rectangle:
    """
    A class representing a rectangle with length and width.
    """

    def __init__(self, length: float, width: float) -> None:
        """
        Initialize a Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        """
        Return a formal string representation of the rectangle.

        Returns:
            str: The rectangle in format 'Rectangle(<length>, <width>)'.
        """
        return f"Rectangle({self.length}, {self.width})"

    def __str__(self) -> str:
        """
        Return an informal string representation of the rectangle.

        Returns:
            str: The rectangle in format 'Rectangle(<length>, <width>)'.
        """
        return self.__repr__()
