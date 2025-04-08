'''
TODO:
    A word is any sequence of one or more Latin letters.

    Implement the Word class that describes a word.

    When creating an instance, the class must accept one argument:
        word — a word

    An instance of the Word class must have the following formal string
    representation:
        Word('<word in its original form>')

    And the following informal string representation:
        <word in which the first letter is uppercase and all the rest
        are lowercase>

    Also, instances of the Word class must support all comparison operations
    between themselves using the operators ==, !=, >, <, >=, <=.

    Two words are considered equal if their lengths are the same.

    A word is considered greater than another word if its length is greater.

NOTE:
    If the object with which the comparison operation is performed is
    incorrect, the method implementing this operation must return
    the NotImplemented constant.

    There are no restrictions regarding the implementation of the Word class,
    it can be arbitrary.
'''
from functools import total_ordering


@total_ordering
class Word:
    """
    A class representing a word as a sequence of Latin letters.
    """

    def __init__(self, word: str) -> None:
        """
        Initialize a Word instance.

        Args:
            word (str): The word as a string of Latin letters.
        """
        self.word = word

    def __repr__(self) -> str:
        """
        Return a formal string representation of the word.

        Returns:
            str: The word in format "Word('<word>')".
        """
        return f"Word('{self.word}')"

    def __str__(self) -> str:
        """
        Return an informal string representation of the word.

        Returns:
            str: The word with the first letter uppercase and the rest
                 lowercase.
        """
        return self.word.capitalize()

    def __eq__(self, value: object) -> bool:
        """
        Compare the word with another word for equality based on length.

        Args:
            value (object): The object to compare with (expected to be Word).

        Returns:
            bool: True if lengths match, False otherwise.
            NotImplemented: If the comparison is not supported.
        """
        if isinstance(value, Word):
            return len(self.word) == len(value.word)
        return NotImplemented

    def __lt__(self, value: object) -> bool:
        """
        Compare the word with another word for less-than based on length.

        Args:
            value (object): The object to compare with (expected to be Word).

        Returns:
            bool: True if length is less, False otherwise.
            NotImplemented: If the comparison is not supported.
        """
        if isinstance(value, Word):
            return len(self.word) < len(value.word)
        return NotImplemented
