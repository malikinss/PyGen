'''
TODO:
    A word is any sequence of one or more letters.

    A text is a set of words separated by whitespace.

    Implement a TextHandler class that describes an initially empty,
    extensible set of words.

    When instantiated, the class must not take any arguments.

    A TextHandler instance must have three methods:
        - add_words() — a method that takes text as an argument and adds words
        from the given text to the set
        - get_shortest_words() — a method that returns the current list of the
        shortest words in the set
        - get_longest_words() — a method that returns the current list of the
        longest words in the set

NOTE:
    The words in the lists returned by get_shortest_words() and
    get_longest_words() must be in the order in which they were added
    to the set.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''
import re
from typing import List


class TextHandler:
    """
    A class representing an extensible collection of words.

    This class maintains a list of words extracted from text and provides
    methods to add words and retrieve the shortest and longest words in the
    order they were added.

    Attributes:
        words (list[str]): A list storing the words added to the collection.

    Methods:
        add_words(text): Adds words from the given text to the collection.
        get_shortest_words(): Returns a list of the shortest words.
        get_longest_words(): Returns a list of the longest words.
    """

    def __init__(self) -> None:
        """
        Initialize a TextHandler instance with an empty list.

        Sets up the collection with an empty list to store words.

        Returns:
            None
        """
        self.words: List[str] = []

    def add_words(self, text: str) -> None:
        """
        Add words from the given text to the collection.

        Extracts words (sequences of letters) from the text and appends them
        to the internal list.

        Args:
            text (str): The text containing words to add.

        Returns:
            None
        """
        # Extract words using regex: one or more letters (Latin or Cyrillic)
        extracted_words = re.findall(r'\b[a-zA-Zа-яА-ЯёЁ]+\b', text)
        self.words.extend(extracted_words)

    def _get_word_lengths(self) -> List[int]:
        """
        Return a list of lengths of all words in the collection.

        Computes the length of each word in the internal list.

        Returns:
            list[int]: A list of word lengths.
        """
        return [len(word) for word in self.words]

    def _is_length_equal(self, word: str, target_length: int) -> bool:
        """
        Check if the word's length equals the target length.

        Args:
            word (str): The word to check.
            target_length (int): The length to compare against.

        Returns:
            bool: True if the word's length equals the target length,
            False otherwise.
        """
        return len(word) == target_length

    def _filter_by_length(self, target_length: int) -> List[str]:
        """
        Return a list of words matching the target length.

        Filters the collection to include only words with the specified length,
        preserving their original order.

        Args:
            target_length (int): The length to filter by.

        Returns:
            list[str]: A list of words with the specified length.
        """
        return list(
            filter(
                lambda word: self._is_length_equal(word, target_length),
                self.words
            )
        )

    def get_shortest_words(self) -> List[str]:
        """
        Return a list of the shortest words in the collection.

        Retrieves all words with the minimum length in their original order.
        Returns an empty list if the collection is empty.

        Returns:
            list[str]: A list of the shortest words.
        """
        if not self.words:
            return []
        min_length = min(self._get_word_lengths())
        return self._filter_by_length(min_length)

    def get_longest_words(self) -> List[str]:
        """
        Return a list of the longest words in the collection.

        Retrieves all words with the maximum length in their original order.
        Returns an empty list if the collection is empty.

        Returns:
            list[str]: A list of the longest words.
        """
        if not self.words:
            return []
        max_length = max(self._get_word_lengths())
        return self._filter_by_length(max_length)
