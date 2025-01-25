'''
TODO:
    Write a program that uses the random module to generate a random password.

    The program takes the length of the password as input and outputs a random
    password containing only the English characters a..z, A..Z (lower and
    upper case).

NOTE:
    The English characters A..Z correspond to numbers 65 through 90
    in the ASCII character table.

    The English characters a..z correspond to numbers 97 through 122
    in the ASCII character table.

    Use the chr() function to get a character by its ASCII character number.

    For example, with a password length of 15 characters, your program
    might output:
        peJFAmhqfaAeKDu
'''
import random


def get_random_uppercase_letter() -> str:
    """
    Returns a random uppercase English letter (A..Z).

    Returns:
        str: A random uppercase letter.
    """
    return chr(random.randint(65, 90))


def get_random_lowercase_letter() -> str:
    """
    Returns a random lowercase English letter (a..z).

    Returns:
        str: A random lowercase letter.
    """
    return chr(random.randint(97, 122))


def generate_random_password(length: int) -> str:
    """
    Generates a random password of a given length using only English characters
    (a..z, A..Z in both lower and upper case).

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A randomly generated password.
    """
    password = []

    for _ in range(length):
        if random.randint(1, 2) == 1:
            password.append(get_random_uppercase_letter())
        else:
            password.append(get_random_lowercase_letter())

    return ''.join(password)


def run_password_generator() -> None:
    """
    Runs the password generator by taking the desired password length as input
    and printing the generated password.

    Returns:
        None
    """
    length = int(input("Enter the desired password length: "))
    password = generate_random_password(length)
    print(password)


# Start the password generator
run_password_generator()
