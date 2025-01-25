'''
TODO:
    Write a program that uses the random module to generate n passwords of
    length m characters, consisting of lowercase and uppercase English letters
    and numbers, except for those that are easy to confuse:
        "l" (lowercase L);
        "I" (uppercase i);
        "1" (digit);
        "o" and "O" (lowercase and uppercase letters);
        "0" (digit).

NOTE:
    Assume that the numbers n and m are always such that the required
    passwords can be generated.

    Each password does not necessarily have to contain at least one digit and
    letter in uppercase and lowercase.
'''
import string
import random


def is_available(char: str, forbidden_symbols: str) -> bool:
    """
    Checks if a given symbol is available (not excluded).

    Args:
        char (str): The symbol to check.
        forbidden_symbols (str): A string of symbols to exclude.

    Returns:
        bool: True if the symbol is available, False if it is excluded.
    """
    return char not in forbidden_symbols


def get_available_symbols(forbidden_symbols: str) -> str:
    """
    Returns a string containing available symbols after excluding the not
    available ones.

    Args:
        forbidden_symbols (str): A string of symbols to exclude from the
                                 available options.

    Returns:
        str: A string containing available symbols for password generation.
    """
    # Define all possible characters: letters (lowercase and uppercase)
    # and digits
    symbols = string.ascii_letters + string.digits

    # Filter out the excluded symbols
    filtered_symbols = [
        char for char in symbols if is_available(char, forbidden_symbols)
    ]

    return ''.join(filtered_symbols)


def generate_password(length: int, available_symbols: str) -> str:
    """
    Generates a random password of a given length using available symbols.

    Args:
        length (int): The length of the password.
        available_symbols (str): A string of symbols from which the password
                                 will be generated.

    Returns:
        str: The generated password.
    """
    pswd = ''.join(random.choice(available_symbols) for _ in range(length))
    return pswd


def generate_passwords(
    count: int, length: int, available_symbols: str
) -> list[str]:
    """
    Generates a list of random passwords.

    Args:
        count (int): The number of passwords to generate.
        length (int): The length of each password.
        available_symbols (str): A string of symbols from which the passwords
                                 will be generated.

    Returns:
        list[str]: A list of generated passwords.
    """
    return [generate_password(length, available_symbols) for _ in range(count)]


# Main execution
n, m = int(input()), int(input())

# Define the symbols to exclude
excluded_symbols = "lI10Oo"

# Get the available symbols excluding the ones defined
available_symbols = get_available_symbols(excluded_symbols)

# Generate the passwords
new_passwords = generate_passwords(n, m, available_symbols)

# Print each password on a new line
print(*new_passwords, sep='\n')
