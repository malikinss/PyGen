'''
TODO:
    Implement a class Strip, instances of which allow you to remove certain
    characters from the beginning and end of a string.

    When instantiated, the class must accept one argument:
        chars — a string listing the characters to be removed

    An instance of the Strip class must be a callable object and must accept
    one argument:
        string — a string

    An instance of the Strip class must remove all characters listed in chars
    from the beginning and end of the string string and return the result.

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Strip class,
    it can be arbitrary.
'''


class Strip:
    """
    A class for stripping specified characters from the beginning and end of
    a string.
    """

    def __init__(self, chars: str) -> None:
        """
        Initialize Strip with characters to remove.

        Args:
            chars (str): A string listing the characters to be removed.
        """
        self.chars = chars

    def __call__(self, string: str) -> str:
        """
        Remove specified characters from the beginning and end of the string.

        Args:
            string (str): The string to strip.

        Returns:
            str: The string with characters from self.chars removed from both
                 ends.
        """
        return string.strip(self.chars)
