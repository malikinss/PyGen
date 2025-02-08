'''
TODO:
    Given a list of words, add the code after the unpacking operator (*),
    which wraps all the elements of the words list in double quotes and then
    prints the result on one line separated by a space.
'''


def print_quoted_words(words: list) -> None:
    """
    Prints all words in the given list, each wrapped in double quotes,
    separated by a space.

    Parameters:
    - words (list): A list of words to be printed.
    """
    print(*map(lambda x: f'"{x}"', words), sep=' ')


# Example usage:
words = 'the world is mine take a look what you have started'.split()
print_quoted_words(words)
