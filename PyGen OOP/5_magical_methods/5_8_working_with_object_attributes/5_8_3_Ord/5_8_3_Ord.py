'''
TODO:
    Implement the Ord class.

    The class must not take any arguments when instantiated.

    An instance of the Ord class must act as an alternative to the ord()
    function.

    When accessing an instance attribute whose name is a single character,
    its position in the Unicode character table must be returned.

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Ord class,
    it can be arbitrary.
'''
from typing import Any


class Ord:
    """
    A class that mimics ord() for single-character attribute names.
    """

    def __init__(self) -> None:
        """
        Initialize an empty Ord instance.
        """
        pass

    def __getattribute__(self, name: str) -> Any:
        """
        Return the Unicode code point for a single-character attribute name.

        Args:
            name (str): The name of the attribute.

        Returns:
            int: The Unicode code point if name is a single character.

        Raises:
            AttributeError: If the attribute name is not a single character.
        """
        if len(name) == 1:
            return ord(name)
        raise AttributeError(f"'{name}' is not a single character")
