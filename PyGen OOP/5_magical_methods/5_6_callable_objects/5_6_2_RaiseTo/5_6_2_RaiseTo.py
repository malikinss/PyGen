'''
TODO:
    Implement a class RaiseTo, instances of which allow raising numbers to
    a fixed power.

    When instantiated, the class must accept one argument:
        degree — the exponent

    An instance of the RaiseTo class must be a callable object and accept
    one argument:
        x — a number

    An instance of the RaiseTo class must return the value of x raised to
    the power of degree.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the RaiseTo
    class, it can be arbitrary.
'''
from typing import Union


class RaiseTo:
    """
    A class for raising numbers to a fixed power.
    """

    def __init__(self, degree: Union[int, float]) -> None:
        """
        Initialize RaiseTo with a fixed exponent.

        Args:
            degree (int | float): The exponent to raise numbers to.
        """
        self.degree = degree

    def __call__(self, x: Union[int, float]) -> Union[int, float]:
        """
        Raise the given number to the fixed power.

        Args:
            x (int | float): The number to raise.

        Returns:
            int | float: The result of x raised to the power of degree.
        """
        return x ** self.degree
