'''
TODO:
    A text file is available to you "file.txt", typed in Latin.

    Write a program that outputs the number of letters of the Latin alphabet,
    words and strings.

    Print the three found numbers in the format given in the example.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''
from string import ascii_letters


def get_output_message(
    letters_number: int, words_number: int, lines_number: int
) -> str:
    """
    Generates the output message that includes the counts of letters, words,
    and lines.

    Parameters:
    - letters_number (int): The number of letters in the file.
    - words_number (int): The number of words in the file.
    - lines_number (int): The number of lines in the file.

    Returns:
    - str: The formatted message containing the counts.
    """
    msg = '\n'.join([
        "Input file contains:",
        str(letters_number) + ' letters',
        str(words_number) + ' words',
        str(lines_number) + ' lines',
    ])

    return msg


def get_data_from_file(file_name: str) -> list[str]:
    """
    Reads all lines from a file and returns them as a list of strings.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - list[str]: A list of strings, each representing a line from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        return [line.rstrip() for line in given_file]


def get_words_number(data: list[str]) -> int:
    """
    Counts the total number of words in the provided data.

    Parameters:
    - data (list[str]): A list of strings, each representing a line of text.

    Returns:
    - int: The total number of words in the data.
    """
    return sum(len(row.split()) for row in data)


def get_letters_number(data: list[str]) -> int:
    """
    Counts the total number of letters (from the Latin alphabet) in the
    provided data.

    Parameters:
    - data (list[str]): A list of strings, each representing a line of text.

    Returns:
    - int: The total number of letters in the data.
    """
    return sum(1 for row in data for char in row if char in ascii_letters)


def get_lines_number(data: list[str]) -> int:
    """
    Counts the total number of lines in the provided data.

    Parameters:
    - data (list[str]): A list of strings, each representing a line of text.

    Returns:
    - int: The total number of lines in the data.
    """
    return len(data)


# Main execution
data = get_data_from_file('file.txt')

letters_number = get_letters_number(data)
words_number = get_words_number(data)
lines_number = get_lines_number(data)

# Print the result
print(get_output_message(letters_number, words_number, lines_number))
