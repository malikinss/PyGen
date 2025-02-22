'''
TODO:
        You can access the text file pythonzen.txt, which contains the
        following text in English:
            The Zen of Python, by Tim Peters

            Beautiful is better than ugly.
            Explicit is better than implicit.
            ...

        Write a program that determines how many times each letter appears in
        this text.

        The letters and their counts should be printed in lexicographic order,
        each on a separate line, in the following format:
            <letter>: <count>

NOTE:
        The initial part of the answer looks like this:
            a: 53
            b: 21
            ...

        The program should not be case-sensitive, that is, for example, the
        letters a and A are considered the same.

        The program should ignore all non-alphabetic characters.
'''
from collections import Counter
import string


def read_lines_from_file(file_name: str) -> list[str]:
    """
    Reads lines from a text file and returns them as a list of strings.

    Args:
        file_name (str): The path to the text file.

    Returns:
        list[str]: A list of lines read from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as file:
        return [line.rstrip() for line in file]


def count_letters(text: list[str]) -> Counter[str]:
    """
    Counts the occurrences of each alphabetic letter in the given text.

    Args:
        text (list[str]): A list of strings representing the text.

    Returns:
        Counter[str]: A Counter object mapping each letter to its count.
    """
    letter_counts = Counter(
        char for line in text
        for char in line.lower() if char in string.ascii_lowercase
    )
    return Counter(dict(sorted(letter_counts.items())))


def display_letter_counts(letter_counts: Counter[str]) -> None:
    """
    Displays the counts of each letter in lexicographic order.

    Args:
        letter_counts (Counter[str]): A Counter object mapping each letter to
        its count.
    """
    for letter, count in letter_counts.items():
        print(f"{letter}: {count}")


if __name__ == "__main__":
    file_path = "./tests/pythonzen.txt"
    display_letter_counts(count_letters(read_lines_from_file(file_path)))
