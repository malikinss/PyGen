'''
TODO:
    Snake Case is a style of writing compound words in which multiple words
    are separated by an underscore (_) and have no spaces in the entry, with
    each word written with a lowercase letter.

    For example, bee_geek and hello_world.

    Upper Camel Case is a style of writing compound words in which multiple
    words are written together without spaces, with each word written with
    a capital letter.

    For example, BeeGeek and HelloWorld.

    Implement a CaseHelper class that describes a set of functions for working
    with strings in the Snake Case and Upper Camel Case styles.

    The class must not take any arguments when instantiated.

    The CaseHelper class must have four static methods:
        - is_snake() — a method that takes a string as an argument and
                       returns True if the passed string is written in
                       Snake Case style, or False otherwise
        - is_upper_camel() — a method that takes a string as an argument and
                             returns True if the passed string is written in
                             Upper Camel Case style, or False otherwise
        - to_snake() — a method that takes a string in Upper Camel Case style
                       as an argument, writes it in Snake Case style,
                       and returns the result
        - to_upper_camel() — a method that takes a string in Snake Case style
                             as an argument, writes it in Upper Camel Case
                             style, and returns the result

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with valid data.
'''
import re


class CaseHelper:
    """
    A class providing static methods for working with Snake Case and
    Upper Camel Case strings.
    """

    @staticmethod
    def is_snake(string: str) -> bool:
        """
        Check if a string is in Snake Case style.

        Args:
            string (str): The input string to check.

        Returns:
            bool: True if the string is in Snake Case (e.g., 'bee_geek'),
                  False otherwise.
        """
        regex = r'^[a-z]+(_[a-z]+)*$'
        return bool(re.fullmatch(regex, string))

    @staticmethod
    def is_upper_camel(string: str) -> bool:
        """
        Check if a string is in Upper Camel Case style.

        Args:
            string (str): The input string to check.

        Returns:
            bool: True if the string is in Upper Camel Case (e.g., 'BeeGeek'),
                  False otherwise.
        """
        regex = r'^([A-Z][a-z0-9]+)+$'
        return bool(re.fullmatch(regex, string))

    @staticmethod
    def to_snake(string: str) -> str:
        """
        Convert an Upper Camel Case string to Snake Case.

        Args:
            string (str): The Upper Camel Case string (e.g., 'BeeGeek').

        Returns:
            str: The string in Snake Case (e.g., 'bee_geek').
        """
        result = re.sub(r'(?<=.)((?=[A-Z]))', '_', string)
        return result.lower()

    @staticmethod
    def to_upper_camel(string: str) -> str:
        """
        Convert a Snake Case string to Upper Camel Case.

        Args:
            string (str): The Snake Case string (e.g., 'bee_geek').

        Returns:
            str: The string in Upper Camel Case (e.g., 'BeeGeek').
        """
        return ''.join(map(str.capitalize, string.split('_')))
