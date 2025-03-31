'''
TODO:
    A word is any sequence of one or more Latin letters.

    Implement a Wordplay class that describes an extensible set of words.

    When instantiated, the class must accept one argument:
        - words — a list defining the initial set of words.
        If not passed, the initial set of words is considered empty

    An instance of the Wordplay class must have one attribute:
        - words — a list containing the set of words

    The Wordplay class must have four instance methods:
        - add_word() — a method that takes a word as an argument and adds it
        to the set.
        If the word is already in the set, the method should do nothing
        - words_with_length() is a method that takes a natural number n as
        an argument and returns a list of words from the set whose length is n
        - only() is a method that takes an arbitrary number of letter
        arguments and returns a list of all words from the set that contain
        only the given letters
        - avoid() is a method that takes an arbitrary number of letter
        arguments and returns a list of all words from the set that do not
        contain any of these letters

NOTE:
    The words in the lists returned by words_with_length(), only(),
    and avoid() must be in the order in which they were added.

    An instance of the Wordplay class must not depend on the list from which
    it was created.

    In other words, if the original list changes, the instance of the Wordplay
    class must not change.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from typing import List


class Wordplay:
    """
    A class representing an extensible set of words.

    This class maintains a list of unique words and provides methods
    to add words and filter them based on length or letter constraints,
    preserving the order of addition.

    Attributes:
        words (list[str]): A list containing the set of words.

    Methods:
        add_word(word): Adds a word to the set if not already present.
        words_with_length(n): Returns words of the specified length.
        only(*args): Returns words containing only the given letters.
        avoid(*args): Returns words not containing any of the given
            letters.
    """

    def __init__(self, words: List[str] | None = None) -> None:
        """
        Initialize a Wordplay instance with an optional list of words.

        Creates a copy of the provided list or an empty list if none
        is given.

        Args:
            words (list[str] | None): Initial list of words, defaults
                to None.

        Returns:
            None
        """
        self.words = [] if words is None else words.copy()

    def add_word(self, word: str) -> None:
        """
        Add a word to the set if it is not already present.

        Appends the word to the list only if it does not exist in
        the set.

        Args:
            word (str): The word to add.

        Returns:
            None
        """
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int) -> List[str]:
        """
        Return a list of words with the specified length.

        Filters the set for words of length n, preserving their order.

        Args:
            n (int): The length to filter by.

        Returns:
            list[str]: A list of words with length n.
        """
        return [
            word
            for word in self.words
            if len(word) == n
        ]

    def only(self, *args: str) -> List[str]:
        """
        Return a list of words containing only the given letters.

        Filters the set for words made up exclusively of the specified
        letters, preserving their order.

        Args:
            *args (str): Variable number of letters.

        Returns:
            list[str]: A list of matching words.
        """
        allowed_letters = set(args)
        matching_words = [
            word
            for word in self.words
            if self._is_word_made_of_letters(
                word, allowed_letters
            )
        ]
        return matching_words

    def _is_word_made_of_letters(
        self, word: str, allowed_letters: set
    ) -> bool:
        """
        Check if a word is made up exclusively of the allowed letters.

        Args:
            word (str): The word to check.
            allowed_letters (set): The set of allowed letters.
            allowed_count (int): The number of allowed letters.

        Returns:
            bool: True if the word uses only the allowed letters, False
                otherwise.
        """
        word_letters = set(word)
        return word_letters.issubset(allowed_letters)

    def avoid(self, *args: str) -> List[str]:
        """
        Return a list of words not containing any of the given letters.

        Filters the set for words that exclude all specified letters,
        preserving their order.

        Args:
            *args (str): Variable number of letters to avoid.

        Returns:
            list[str]: A list of matching words.
        """
        forbidden_letters = set(args)
        return [
            word
            for word in self.words
            if all(
                letter not in forbidden_letters
                for letter in word
            )
        ]
