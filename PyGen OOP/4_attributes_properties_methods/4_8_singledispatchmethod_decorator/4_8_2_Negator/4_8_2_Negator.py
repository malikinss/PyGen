'''
TODO:
    Implement the Negator class.

    The class must not take any arguments when instantiated.

    The Negator class must have one static method:
        - neg() — a method that takes an object as an argument and returns
                  its opposite.

    If the method is passed an integer or a real number, it must return this
    number taken with the opposite sign.

    If the method is passed a boolean value as an argument, it must return
    the boolean value that is the opposite of the passed one.

    If the passed object belongs to some other type, a TypeError exception
    must be raised with the text:
        Argument of the passed type is not supported

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the Negator class, it can be arbitrary.
'''
from functools import singledispatchmethod


class Negator:
    """
    A class for negating objects based on their type.
    """

    @singledispatchmethod
    @staticmethod
    def neg(obj: object) -> None:
        """
        Negate an object based on its type.

        Args:
            obj (object): The object to negate.

        Raises:
            TypeError: If the type of the object is not supported.
        """
        raise TypeError("Argument of the passed type is not supported")

    @neg.register
    @staticmethod
    def _neg_number(obj: int | float) -> int | float:
        """
        Negate a number by changing its sign.

        Args:
            obj (int | float): The number to negate.

        Returns:
            int | float: The number with the opposite sign.
        """
        return -obj

    @neg.register
    @staticmethod
    def _neg_boolean(obj: bool) -> bool:
        """
        Negate a boolean value.

        Args:
            obj (bool): The boolean value to negate.

        Returns:
            bool: The opposite boolean value.
        """
        return not obj
