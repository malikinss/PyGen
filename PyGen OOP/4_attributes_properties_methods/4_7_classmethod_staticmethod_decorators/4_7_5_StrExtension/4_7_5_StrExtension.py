'''
TODO:
    Implement the StrExtension class, which describes a set of functions for
    working with strings.

    When creating an instance, the class must not take any arguments.

    The StrExtension class must have three static methods:
        - remove_vowels() — a method that takes a string as an argument,
                            removes all Latin vowels from it, case-insensitive,
                            and returns the result
        - leave_alpha() — a method that takes a string as an argument, removes
                          all non-Latin characters from it, and returns
                          the result
        - replace_all() — a method that takes three string arguments string,
                          chars, and char, replaces all characters from chars
                          with char in string, case-sensitive, and returns
                          the result.

NOTE:
    It is guaranteed that all alphabetic characters belong to
    the Latin alphabet.

    Latin vowels: a, e, i, o, u, y.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''
import re


class StrExtension:
    """
    A class providing static methods for string manipulation.
    """
    VOWELS = 'aeiouy'
    ALPHA = 'a-zA-Z'

    @staticmethod
    def remove_vowels(string: str) -> str:
        """
        Remove all Latin vowels from a string, case-insensitive.

        Args:
            string (str): The input string.

        Returns:
            str: The string with all vowels removed.
        """
        return re.sub(fr'[{StrExtension.VOWELS}]', '', string, flags=re.I)

    @staticmethod
    def leave_alpha(string: str) -> str:
        """
        Remove all non-Latin alphabetic characters from a string.

        Args:
            string (str): The input string.

        Returns:
            str: The string containing only Latin alphabetic characters.
        """
        return re.sub(fr'[^{StrExtension.ALPHA}]', '', string)

    @staticmethod
    def replace_all(string: str, chars: str, char: str) -> str:
        """
        Replace all specified characters in a string with a single character.

        Args:
            string (str): The input string.
            chars (str): The characters to replace.
            char (str): The character to replace with.

        Returns:
            str: The modified string.
        """
        return re.sub(fr'[{chars}]', char, string)
