'''
TODO:
    Implement an Alphabet class that produces iterators whose constructor
    takes one argument:
        language — language code:
            ru — Russian
            en — English

    The Alphabet() class iterator should cyclically generate a sequence of
    lowercase letters:
        of the Russian alphabet, if language is ru
        of the English alphabet, if language is en
NOTE:
    The letter ё is not taken into account in the Russian alphabet.
'''
import string
from typing import Iterator


class Alphabet:
    def __init__(self, language: str) -> None:
        """
        Initialize the Alphabet iterator based on the selected language.

        Args:
            language (str): The language code, either 'ru' (Russian)
            or 'en' (English).

        Raises:
            ValueError: If an unsupported language is provided.
        """
        if language not in ['ru', 'en']:
            raise ValueError(
                "Unsupported language. Choose 'ru' or 'en'."
            )

        self._lang = language
        self._alphabets = {
            'en': string.ascii_lowercase,
            'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        }

        # Initialize the iterator
        self._alphabet = iter(self._alphabets[self._lang])

    def __iter__(self) -> Iterator[str]:
        """
        Return the iterator object.

        Returns:
            Iterator[str]: The iterator over the alphabet letters.
        """
        return self

    def __next__(self) -> str:
        """
        Get the next letter in the alphabet.
        Once the end is reached, it loops back.

        Returns:
            str: The next letter in the alphabet.

        Raises:
            StopIteration: Never raised due to cyclic behavior.
        """
        try:
            return next(self._alphabet)
        except StopIteration:
            # Reset the iterator to loop back to the beginning of the alphabet
            self._alphabet = iter(self._alphabets[self._lang])
            return next(self._alphabet)
