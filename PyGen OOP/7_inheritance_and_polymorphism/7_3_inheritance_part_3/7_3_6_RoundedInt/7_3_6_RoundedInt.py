'''
TODO:
    The nearest even number for an odd integer n is n + 1, and the nearest
    even number for an even integer is itself.

    Similarly, the nearest odd number for an even integer n is n + 1, and
    the nearest odd number for an odd integer is itself.

    Implement a RoundedInt class that inherits from the int class and
    describes an integer that is automatically rounded to the nearest even or
    odd number when created.

    When instantiated, the class must accept two arguments in the following
    order:
        num — an object defining the numeric value of the RoundedInt instance
        even — a Boolean value that defines the parity when rounding.
               If True, rounding occurs to the nearest even number.
               If False, rounding occurs to the nearest odd number.
               True by default

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the RoundedInt
    class, it can be arbitrary.
'''
from typing import Any


class RoundedInt(int):
    """
    Class representing an integer rounded to the nearest even or odd number.

    Inherits from int, with automatic rounding to even or odd based on
    the even parameter.
    """

    def __new__(cls, num: Any, even: bool = True) -> 'RoundedInt':
        """
        Create a new RoundedInt instance with the value rounded to even or odd.

        Args:
            num: The object defining the numeric value.
            even: If True, round to the nearest even number; if False, to
                  the nearest odd number.
                  Defaults to True.

        Returns:
            RoundedInt: A new instance with the rounded value.
        """
        num = int(num)  # Ensure num is an integer
        if num % 2 != (0 if even else 1):
            num += 1
        return super().__new__(cls, num)
