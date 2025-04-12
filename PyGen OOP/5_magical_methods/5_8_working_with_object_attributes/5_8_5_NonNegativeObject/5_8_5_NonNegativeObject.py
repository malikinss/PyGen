'''
TODO:
    Implement the NonNegativeObject class.

    When creating an instance, the class must accept an arbitrary number
    of named arguments.

    All arguments passed must be set to the created instance as attributes,
    and if the attribute value is a negative number, it must be taken with
    the opposite sign.

NOTE:
    Instances of the int and float classes will be considered numbers.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the NonNegativeObject class, it can be arbitrary.
'''
from typing import Any


class NonNegativeObject:
    """
    A class that sets attributes with non-negative numeric values.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize with arbitrary named arguments, making numeric values
        non-negative.

        Args:
            **kwargs: Named arguments to set as attributes. Negative numbers
                      are converted to positive.
        """
        for attr, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                value = -value
            object.__setattr__(self, attr, value)
