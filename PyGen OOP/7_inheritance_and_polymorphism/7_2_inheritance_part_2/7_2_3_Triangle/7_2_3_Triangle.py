'''
TODO:
    Implement a Triangle class that describes a triangle.

    When instantiated, the class must accept three arguments in the following
    order:
        a — the length of a side of the triangle
        b — the length of a side of the triangle
        c — the length of a side of the triangle

    The Triangle class must have one instance method:
        perimeter() — a method that returns the perimeter of the triangle

    Also implement an EquilateralTriangle class, a subclass of Triangle that
    describes an equilateral triangle.

    When instantiated, the class must accept one argument:
        side — the length of a side of the triangle

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of classes, it can
    be arbitrary.
'''


class Triangle:
    """
    Class representing a triangle with three sides.

    This class stores the lengths of the triangle's sides and provides
    a method to calculate its perimeter.
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initialize a Triangle instance.

        Args:
            a: Length of the first side.
            b: Length of the second side.
            c: Length of the third side.
        """
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the triangle.

        Returns:
            float: The sum of the lengths of the triangle's sides.
        """
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    """
    Class representing an equilateral triangle.

    Inherits from Triangle and represents a triangle with all sides of
    equal length.
    """

    def __init__(self, side: float) -> None:
        """
        Initialize an EquilateralTriangle instance.

        Args:
            side: Length of each side of the triangle.
        """
        super().__init__(side, side, side)
