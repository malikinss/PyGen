'''
TODO:
        Implement a function power() that takes one argument:
            degree — an integer

        The function power() should return a function that takes an
        integer x as an argument and returns the value of x raised to
        the power degree.

NOTE:
        Let's look at the example from the first test.

        The call power(2) returns a function that takes a number as an
        argument and raises it to the second power.

        The function is assigned to the variable square.
        The resulting function is then called with the argument 5 and returns
        the value 5**2=25.
'''
from typing import Callable


def power(degree: int) -> Callable:
    """
    Generates a function that raises a number to a specified power.

    Args:
        degree (int): The exponent to which the base number will be raised.

    Returns:
        Callable[[int], int]: A function that raises a number to the power of
        `degree`.
    """
    if not isinstance(degree, int):
        raise ValueError("Degree must be an integer.")

    def raise_to_power(x: int) -> int:
        """
        Raises a number to the specified power.

        Args:
            x (int): The base number to be raised.

        Returns:
            int: The result of `x` raised to the power of `degree`.
        """
        return x ** degree
    return raise_to_power
