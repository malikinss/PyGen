'''
TODO:
    An anagram is a word formed by rearranging the letters that make up
    another word.

    For example, the words saw and linden or post and stop are anagrams.

    Write a program that reads one word and outputs its random anagram using
    the random module.
'''
import random


def generate_anagram(word: str) -> str:
    """
    Generates a random anagram of the given word by rearranging its letters.

    Args:
        word (str): The word for which to generate an anagram.

    Returns:
        str: A random anagram of the input word.
    """
    word_to_list = list(word)
    random.shuffle(word_to_list)
    return ''.join(word_to_list)


# Example usage
word = input()
anagram = generate_anagram(word)
print(anagram)
