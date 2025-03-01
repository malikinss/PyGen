"""
TODO:
    Write a program that outputs all lowercase Latin letters.

    No input is given to the program.

    The program should output all lowercase Latin letters from a to z,
    each on a separate line.

NOTE:
    It is convenient to use the ord() and chr() functions in the task.
"""
from string import ascii_lowercase


def print_lowercase_letters_1() -> None:
    """
    Prints all lowercase Latin letters, each on a separate line using unicode
    manipulation.

    Args:
        None

    Returns:
        None
    """
    for unicode_id in range(ord('a'), ord('z') + 1):
        print(chr(unicode_id))


def print_lowercase_letters_2() -> None:
    """
    Prints all lowercase Latin letters, each on a separate line using
    ascii_lowercase from string module.

    Args:
        None

    Returns:
        None
    """
    for letter in ascii_lowercase:
        print(letter)


def print_lowercase_letters_3() -> None:
    """
    Prints all lowercase Latin letters, each on a separate line using
    unpacking with newline separator.

    Args:
        None

    Returns:
        None
    """
    print(*ascii_lowercase, sep='\n')


print_lowercase_letters_1()
