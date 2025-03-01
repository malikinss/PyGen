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


def print_lowercase_letters() -> None:
    """
    Prints all lowercase Latin letters, each on a separate line using
    different approaches:
    1. Using ord() and chr()
    2. Using ascii_lowercase from string module
    3. Using unpacking with newline separator

    Args:
        None

    Returns:
        None
    """
    # Method 1: Using ord() and chr()
    for unicode_id in range(ord('a'), ord('z') + 1):
        print(chr(unicode_id))

    # Method 2: Using ascii_lowercase from string module
    for letter in ascii_lowercase:
        print(letter)

    # Method 3: Using unpacking with newline separator
    print(*ascii_lowercase, sep='\n')


print_lowercase_letters()
