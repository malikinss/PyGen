'''
TODO:
    You have access to the Processor class.

    The class does not take any arguments when instantiated.

    The Processor class has one static method:
        - process() — a method that takes an arbitrary object as an argument,
                      converts it depending on its type, and returns the
                      result.
                      If the type of the passed object is not supported by
                      the method, a TypeError exception is raised with
                      the text:
                        The argument of the passed type is not supported

    Rewrite the process() method of the Processor class using
    the @singledispatchmethod decorator to perform the same task.

NOTE:
    Examples of converting objects of all supported types are shown in
    the process() method of the Processor class.

    There are no restrictions regarding the implementation of the Processor
    class, it can be arbitrary.
'''
from functools import singledispatchmethod


class Processor:
    """
    A class for processing objects based on their type.
    """

    @singledispatchmethod
    @staticmethod
    def process(data: object) -> None:
        """
        Process an object based on its type.

        Args:
            data (object): The object to process.

        Raises:
            TypeError: If the type of the object is not supported.
        """
        raise TypeError("The argument of the passed type is not supported")

    @process.register
    @staticmethod
    def _process_number(data: int | float) -> int | float:
        """
        Process a number by doubling it.

        Args:
            data (int | float): The number to process.

        Returns:
            int | float: The doubled value.
        """
        return data * 2

    @process.register
    @staticmethod
    def _process_string(data: str) -> str:
        """
        Process a string by converting it to uppercase.

        Args:
            data (str): The string to process.

        Returns:
            str: The uppercase string.
        """
        return data.upper()

    @process.register
    @staticmethod
    def _process_list(data: list) -> list:
        """
        Process a list by sorting it.

        Args:
            data (list): The list to process.

        Returns:
            list: The sorted list.
        """
        return sorted(data)

    @process.register
    @staticmethod
    def _process_tuple(data: tuple) -> tuple:
        """
        Process a tuple by sorting it and returning a new tuple.

        Args:
            data (tuple): The tuple to process.

        Returns:
            tuple: The sorted tuple.
        """
        return tuple(sorted(data))
