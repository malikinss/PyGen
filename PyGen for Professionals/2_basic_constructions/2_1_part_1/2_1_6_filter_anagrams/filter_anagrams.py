'''
TODO:
    Anagrams are words that consist of identical letters.

    Implement the filter_anagrams() function, which takes two arguments in the
    following order:

        word — lowercase word
        words — a list of words in lowercase

    The function should return a list, the elements of which are words from
    the words list, which represent an anagram of the word word.

    If the words list is empty or does not contain anagrams, the function
    should return an empty list.

NOTE:
    The words in the list returned by the function must be in their original
    order.

    Consider the word to be an anagram of itself.
'''


def filter_anagrams(word: str, words: list) -> list:
    """
    Filters the list of words to find anagrams of the given word.

    Args:
        word (str): The word to compare.
        words (list): The list of words to check for anagrams.

    Returns:
        list: A list of words that are anagrams of the given word.
    """
    return [w for w in words if sorted(w) == sorted(word)]
