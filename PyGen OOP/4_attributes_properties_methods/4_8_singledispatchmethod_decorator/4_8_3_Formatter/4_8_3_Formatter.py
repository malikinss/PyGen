'''
TODO:
    Implement the Formatter class.

    The class must not take any arguments when instantiated.

    The Formatter class must have one static method:
        format() — a method that takes an object of type int, float, tuple,
                   list, or dict as an argument and outputs information about
                   the passed object in a format that depends on its type.

    If the passed object belongs to any other type, a TypeError exception must
    be raised with the text:
        Argument of the passed type is not supported

NOTE:
    Examples of formatting objects of all types are shown in the test data.

    Note that the format() method must enclose the string elements of
    the collections in apostrophes.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions on the implementation of the Formatter class,
    it can be arbitrary.
'''
from functools import singledispatchmethod


class Formatter:
    """
    A class for formatting objects based on their type.
    """
    @staticmethod
    def _format_value(value: object) -> str:
        """
        Format a single value, enclosing strings in apostrophes.

        Args:
            value (object): The value to format.

        Returns:
            str: The formatted value, e.g., "'abc'" for strings,
                 "5" for others.
        """
        return f"'{value}'" if isinstance(value, str) else str(value)

    @staticmethod
    def _format_list_or_tuple(obj: list | tuple) -> str:
        """
        Format elements of a list or tuple.

        Args:
            obj (list | tuple): The list or tuple to format.

        Returns:
            str: The formatted elements, e.g., "'a', 1, 2.5".
        """
        return ", ".join(Formatter._format_value(x) for x in obj)

    @singledispatchmethod
    @staticmethod
    def format(obj: object) -> None:
        """
        Format an object based on its type.

        Args:
            obj (object): The object to format.

        Raises:
            TypeError: If the type of the object is not supported.
        """
        raise TypeError("Argument of the passed type is not supported")

    @format.register
    @staticmethod
    def _format_int(obj: int) -> None:
        """
        Format and print an integer.

        Args:
            obj (int): The integer to format.
        """
        print(f"Integer: {obj}")

    @format.register
    @staticmethod
    def _format_float(obj: float) -> None:
        """
        Format and print a float.

        Args:
            obj (float): The float to format.
        """
        print(f"Float: {obj}")

    @format.register
    @staticmethod
    def _format_list(obj: list) -> None:
        """
        Format and print a list.

        Args:
            obj (list): The list to format.
        """
        print(f"List: {Formatter._format_list_or_tuple(obj)}")

    @format.register
    @staticmethod
    def _format_tuple(obj: tuple) -> None:
        """
        Format and print a tuple.

        Args:
            obj (tuple): The tuple to format.
        """
        print(f"Tuple: {Formatter._format_list_or_tuple(obj)}")

    @format.register
    @staticmethod
    def _format_dict(obj: dict) -> None:
        """
        Format and print a dictionary.

        Args:
            obj (dict): The dictionary to format.
        """
        formatted = ", ".join(
            f"({Formatter._format_value(k)}, {Formatter._format_value(v)})"
            for k, v in obj.items()
        )
        print(f"Dict: {formatted}")
