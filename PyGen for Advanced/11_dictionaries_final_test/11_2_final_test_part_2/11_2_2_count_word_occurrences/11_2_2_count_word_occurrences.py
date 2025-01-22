'''
TODO:
    A line of text in Russian is given, consisting of words and space
    characters.

    A word is a sequence of letters, words are separated by one or more spaces.

NOTE:
    The number of numbers must match the number of words in the original text.
'''


def count_word_occurrences(text: str) -> list:
    """
    Counts the occurrences of each word in the given text and returns a list
    of counts.

    Args:
        text (str): A string of text containing words separated by spaces.

    Returns:
        list: A list of integers representing the occurrence count of
              each word in the order they appear.
    """
    given_words_list = [word for word in text.split()]
    count_words: dict = {}
    words_to_print = []

    for word in given_words_list:
        count_words[word] = count_words.get(word, 0) + 1
        words_to_print.append(count_words[word])

    return words_to_print


# Example usage:
given_text = input("Enter a line of text: ").strip()
occurrences = count_word_occurrences(given_text)
print(*occurrences)
