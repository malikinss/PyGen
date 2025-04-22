'''
TODO:
    Implement a class LowerString, a subclass of str, that describes a string
    that is automatically converted to lowercase when created.

    When instantiated, the class must accept one argument:
        obj — an object that defines the initial value of the string.

    Can be omitted, in which case the initial value is considered an empty
    string

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the LowerString
    class, it can be arbitrary.
'''
from typing import Any


class LowerString(str):
    """
    Class representing a string automatically converted to lowercase.

    Inherits from str and converts the initial value to lowercase upon
    creation.
    """

    def __new__(cls, obj: Any = '') -> 'LowerString':
        """
        Create a new LowerString instance with the value converted to
        lowercase.

        Args:
            obj: The object defining the initial string value, defaults to
                 an empty string.

        Returns:
            LowerString: A new instance with the lowercase string value.
        """
        return super().__new__(cls, str(obj).lower())
