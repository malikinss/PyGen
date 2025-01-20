'''
TODO:
    Complete the above code using the generator to obtain a dictionary result,
    in which the key is a string - an element of the words list, and the value
    is a list of the corresponding ASCII codes of the characters in this
    string.

NOTE:
    If the words list were words = ['yes', 'hello'], then the result would be
    a dictionary:
        result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}

    There is no need to output the contents of the result dictionary.
'''
from typing import List, Dict


def get_ascii_codes(words: List[str]) -> Dict[str, List[int]]:
    """
    This function takes a list of words and returns a dictionary where each
    word is mapped to a list of ASCII values of its characters.

    Args:
        words (List[str]): A list of words to convert to dictionaries with
                           ASCII codes.

    Returns:
        Dict[str, List[int]]: A dictionary where each key is a word from the
                              input list, and the value is a list of ASCII
                              values for the characters of that word.
    """
    # Using a dictionary comprehension to generate the result
    return {word: [ord(char) for char in word] for word in words}


# List of words to be processed
words = [
    'hello', 'bye', 'yes', 'no', 'python',
    'apple', 'maybe', 'stepik', 'beegeek'
]

# Calling the function and storing the result
result = get_ascii_codes(words)
