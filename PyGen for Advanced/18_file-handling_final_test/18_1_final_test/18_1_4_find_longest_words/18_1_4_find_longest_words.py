'''
TODO:
    A text file is available to you "words.txt " with words separated
    by a space.

    Write a program that finds and outputs the longest words of this file
    without changing their order.

NOTE:
    Assume that the executable program and the specified file are in the same
    folder.

    Consider any group of characters without spaces as a word, even if it
    includes numbers or punctuation marks.
'''


def read_line_from_file(file_name: str):
    """
    Reads the content of the file and returns a single line without trailing
    newline characters.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: A string representing the line of text from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        return given_file.readline().rstrip()


def find_longest_words(file_name: str):
    """
    Finds the longest words from the file without changing their order.

    Args:
        file_name (str): The name of the file containing the words.

    Returns:
        list: A list of the longest words in the file.
    """
    words = read_line_from_file(file_name).split()

    if not words:  # Handle the case where the file is empty
        return []

    max_len = max(len(word) for word in words)
    return [word for word in words if len(word) == max_len]


# Output the longest words
longest_words = find_longest_words('words.txt')
print(*longest_words, sep='\n')
