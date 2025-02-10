'''
TODO:
    Write a program that finds all similar words for a given word.

    Words are called similar if they have the same number and arrangement of
    vowel letters.

    At the same time, the vowels themselves may differ.

    The program is given one word written in the first line, then a natural
    number n — the number of words to compare and n lines with words.

    The program should output all similar words for a given word, preserving
    their original order.

NOTE:
    After the last vowel, there can be any number of consonants in the initial
    and checked word.

    In Russian, there are 10 vowel letters:
        (а, у, о, ы, и, э, я, ю, ё, е)
    and
    21 consonant letters:
        (б, в, г, д, ж, з, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш).
'''
from typing import List


def create_vowel_consonant_pattern(
    word: str, vowels: set, consonants: set
) -> str:
    """
    Creates a pattern representing the arrangement of vowels ('v') and
    consonants ('c') in a given word.

    Args:
        word (str): The input word to analyze.
        vowels (set): Set of vowel letters.
        consonants (set): Set of consonant letters.

    Returns:
        str: A pattern string where 'v' represents vowels and 'c' represents
             consonants.
    """
    return ''.join(
        'v' if letter in vowels else 'c'
        for letter in word.lower()
        if letter in vowels or letter in consonants
    )


def get_list_of_words(quantity_of_words: int) -> List[str]:
    """
    Reads a specified number of words from the user input.

    Args:
        quantity_of_words (int): The number of words to input.

    Returns:
        list: List of entered words.
    """
    return [input() for _ in range(quantity_of_words)]


def is_word_similar_to_pattern(
    word: str, pattern: str, vowels: set, consonants: set
) -> bool:
    """
    Checks if a word matches the given vowel-consonant pattern.

    Args:
        word (str): The word to check.
        pattern (str): The pattern to compare against.
        vowels (set): Set of vowel letters.
        consonants (set): Set of consonant letters.

    Returns:
        bool: True if the word matches the pattern, False otherwise.
    """
    return create_vowel_consonant_pattern(word, vowels, consonants) == pattern


def find_similar_words_by_vowels(
    word_to_compare: str, vowels: set, consonants: set
) -> List[str]:
    """
    Finds all words that match the vowel-consonant pattern of the given word.

    Args:
        word_to_compare (str): The word to compare other words against.
        vowels (set): Set of vowel letters.
        consonants (set): Set of consonant letters.

    Returns:
        list: A list of words that match the vowel-consonant pattern.
    """
    # Generate the pattern of vowels and consonants for the given word
    pattern = create_vowel_consonant_pattern(
        word=word_to_compare,
        vowels=vowels,
        consonants=consonants
    )

    # Get the number of words to compare and the list of words
    n = int(input())
    words = get_list_of_words(n)

    # Filter words that match the vowel-consonant pattern
    similar_words = [
        word for word in words
        if is_word_similar_to_pattern(word, pattern, vowels, consonants)
    ]

    return similar_words


# Define sets of vowel and consonant letters in Russian
RU_VOWELS = set([
    'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'
])
RU_CONSONANTS = set([
    'б', 'в', 'г', 'д', 'ж', 'з', 'й',
    'к', 'л', 'м', 'н', 'п', 'р', 'с',
    'т', 'ф', 'х', 'ц', 'ч', 'ш'
])

# Input and processing
word_to_compare = input()  # The word to compare
result = find_similar_words_by_vowels(
    word_to_compare, RU_VOWELS, RU_CONSONANTS
)

# Print the result
if result:
    print(*result, sep='\n')
else:
    print("No similar words found.")
