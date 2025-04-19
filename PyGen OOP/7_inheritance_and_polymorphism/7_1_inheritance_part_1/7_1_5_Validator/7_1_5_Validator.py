'''
TODO:
    Implement the Validator class, which describes an object that checks
    a value for correctness.

    When creating an instance, the class must accept one argument:
        obj — an arbitrary object

    The Validator class must have one instance method:
        is_valid() — an empty method that always returns None

    Also implement the NumberValidator class, a descendant of the Validator
    class, which describes an object that checks a value for belonging to
    the int or float type.

    The process of creating an instance of the NumberValidator class must
    coincide with the process of creating an instance of the Validator class.

    The NumberValidator class must have one instance method:
        is_valid() — a method that returns True if the value passed to
                     the initializer belongs to the int or float type,
                     or False otherwise

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of classes, it can
    be arbitrary.
'''
from typing import Any


class Validator:
    """
    Class representing a validator for checking the correctness of a value.

    This class stores an arbitrary object and provides a method to check its
    validity, returning None by default.
    """

    def __init__(self, obj: Any) -> None:
        """
        Initialize a Validator instance.

        Args:
            obj: An arbitrary object to be validated.
        """
        self.obj = obj

    def is_valid(self) -> None:
        """
        Check if the stored object is valid.

        Returns:
            None: Always returns None as a default validation result.
        """
        return None


class NumberValidator(Validator):
    """
    Class representing a validator for checking if a value is a number.

    Inherits from Validator and checks if the stored object is of type int
    or float.
    """

    def is_valid(self) -> bool:
        """
        Check if the stored object is an integer or float.

        Returns:
            bool: True if the object is of type int or float, False otherwise.
        """
        return isinstance(self.obj, (int, float))
