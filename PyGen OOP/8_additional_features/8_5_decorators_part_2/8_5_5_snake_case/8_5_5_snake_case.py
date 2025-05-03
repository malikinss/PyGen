'''
TODO:
    Snake Case is a style of writing compound words in which multiple words
    are separated by an underscore (_) and have no spaces in the notation, and
    each word is written with a lowercase letter.

    For example, bee_geek and hello_world.

    Camel Case is a style of writing compound words in which multiple words
    are written together without spaces, and each word is written with
    a capital letter.

    For example, BeeGeek and HelloWorld.

    A special case of the Camel Case style is lower Camel Case, when all words
    except the first letter are written with a capital letter.

    For example, beeGeek and helloWorld.

    Implement the @snake_case decorator to decorate the class.

    The decorator must take one argument:
        attrs - a boolean value, by default equals False

    The decorator must rename all non-magic methods in the decorated class,
    changing their writing style from Camel Case and lower Camel Case
    to Snake Case.

    The attrs parameter should determine whether the class attributes should
    be similarly renamed.

    If it is True, the style of writing the class attribute names should
    change from Camel Case and lower Camel Case to Snake Case, if False,
    it should remain the same.

NOTE:
    It is guaranteed that the names of all non-magic methods and attributes in
    the class are written in Camel Case, lower Camel Case, or Snake Case.
'''
import re
from typing import Type, TypeVar

T = TypeVar("T")


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
            string: The input string to check.

        Returns:
            bool: True if the string is in Snake Case (e.g., 'bee_geek'),
                  False otherwise.
        """
        regex = r'^[a-z]+(_[a-z]+)*$'
        return bool(re.fullmatch(regex, string))

    @staticmethod
    def is_camel(string: str) -> bool:
        """
        Check if a string is in camel case style.

        Args:
            string: The input string to check.

        Returns:
            bool: True if the string is in camel case,
                  False otherwise.
        """
        stripped = string.lstrip('_')
        regex = r'^[a-z]+([A-Z][a-z0-9]*)*$|^([A-Z][a-z0-9]+)+$'
        return bool(re.fullmatch(regex, stripped))

    @staticmethod
    def is_dunder(string: str) -> bool:
        """
        Check if a string is in dunder (magic method) style.

        Args:
            string: The input string to check.

        Returns:
            bool: True if the string is in dunder style (e.g., '__init__'),
                  False otherwise.
        """
        regex = r'^__\w+__$'
        return bool(re.fullmatch(regex, string))

    @staticmethod
    def _extract_leading_underscores(string: str) -> str:
        """
        Extract leading underscores from string.

        Args:
            string: Input string.

        Returns:
            str: Leading underscores.
        """
        return ''.join(c for c in string if c == '_')

    @staticmethod
    def to_snake(string: str) -> str:
        """
        Convert a Camel Case string to Snake Case, preserving leading
        underscores.

        Args:
            string: Input string (e.g., '_FirstMethod').

        Returns:
            str: String in snake_case with preserved underscores.
        """
        leading_underscores = CaseHelper._extract_leading_underscores(string)
        stripped = string[len(leading_underscores):]
        converted = re.sub(r'(?<=.)((?=[A-Z]))', '_', stripped)
        return leading_underscores + converted.lower()


class snake_case:
    """
    Decorator to convert method and attribute names to snake_case.
    """
    def __init__(self, attrs: bool = False) -> None:
        """
        Init decorator.

        Args:
            attrs: Whether to convert attribute names to snake_case.
        """
        self.attrs = attrs

    def __call__(self, cls: Type[T]) -> Type[T]:
        """
        Rename methods and attributes to snake_case.

        Args:
            cls: Class to decorate.

        Returns:
            Type[T]: Decorated class.
        """
        to_rename = []

        for name, value in cls.__dict__.items():
            is_camel = CaseHelper.is_camel(name)
            is_dunder = CaseHelper.is_dunder(name)

            if is_camel and not is_dunder:
                is_cls_methods = isinstance(value, (classmethod, staticmethod))
                is_method = callable(value) or is_cls_methods
                is_attr = self.attrs and not is_method
                if is_method or is_attr:
                    new_name = CaseHelper.to_snake(name)
                    to_rename.append((name, value, new_name))

        # Perform in-place renaming
        for old_name, value, new_name in to_rename:
            setattr(cls, new_name, value)
            if old_name != new_name:
                try:
                    delattr(cls, old_name)
                except AttributeError:
                    pass

        return cls
