'''
TODO:
    Write a program that uses the random module to generate n passwords of m
    characters each, consisting of lowercase and uppercase English letters and
    numbers, except for those that are easy to confuse:
        "l" (lowercase L);
        "I" (uppercase i);
        "1" (number);
        "o" and "O" (uppercase and lowercase letters);
        "0" (number).

    Additional condition: each password must contain at least one number and
    at least one uppercase and one lowercase letter.

NOTE:
    Assume that the numbers n and m are always such that the required
    passwords can be generated.
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


def generate_password(length):
    """
    Generate a random password of the given length.

    The password contains at least one lowercase letter, one uppercase letter,
    and one digit. It excludes easy-to-confuse characters.

    Args:
        length (int): The length of the password.

    Returns:
        str: The generated password.
    """
    excluded_symbols = 'lI10Oo'
    available_symbols = get_available_symbols(excluded_symbols)

    # Ensure at least one lowercase, one uppercase, and one digit
    password = [
        random.choice(string.ascii_lowercase),   # One lowercase letter
        random.choice(string.ascii_uppercase),   # One uppercase letter
        random.choice(string.digits),            # One digit
    ]

    # Fill the rest of the password with random symbols
    while len(password) < length:
        password.append(random.choice(available_symbols))

    # Shuffle the password to randomize the order
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)


def generate_passwords(count, length):
    """
    Generate a list of random passwords.

    Args:
        count (int): The number of passwords to generate.
        length (int): The length of each password.

    Returns:
        list: A list of generated passwords.
    """
    return [generate_password(length) for _ in range(count)]


# Main execution
n = int(input("Enter number of passwords: "))
m = int(input("Enter length of passwords: "))

new_passwords = generate_passwords(n, m)
print(*new_passwords, sep='\n')
