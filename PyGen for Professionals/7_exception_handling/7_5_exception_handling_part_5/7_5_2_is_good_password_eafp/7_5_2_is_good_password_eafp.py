'''
TODO:
        Let's call a password good if:
            - its length is 9 or more characters
            - it contains upper and lower case letters of any alphabet
            - it contains at least one digit

        Implement an EAFP-style is_good_password() function that takes one
        argument:
            string — an arbitrary string

        The function should return True if string is a good password, or raise
        an exception:
            - LengthError if it is less than 9 characters long
            - LetterError if it contains no letters or all letters have the
            same case
            - DigitError if it contains no digits

        NOTE:
        The LengthError, LetterError, and DigitError exceptions are already
        defined and available.

        The order of raising exceptions when multiple conditions are not met
        is LengthError, then LetterError, and then DigitError.
'''


class PasswordError(Exception):
    pass


class LengthError(Exception):
    pass


class LetterError(Exception):
    pass


class DigitError(Exception):
    pass


def is_sufficient_length(password: str) -> bool:
    """
    Checks if the password length is 9 characters or more.

    Arguments:
        password (str): The password to check.

    Returns:
        bool: True if the password length is >= 9, otherwise False.
    """
    return len(password) >= 9


def has_uppercase(password: str) -> bool:
    """
    Checks if the password contains at least one uppercase letter.

    Arguments:
        password (str): The password to check.

    Returns:
        bool: True if there is at least one uppercase letter, otherwise False.
    """
    return any(char.isupper() for char in password)


def has_lowercase(password: str) -> bool:
    """
    Checks if the password contains at least one lowercase letter.

    Arguments:
        password (str): The password to check.

    Returns:
        bool: True if there is at least one lowercase letter, otherwise False.
    """
    return any(char.islower() for char in password)


def has_digit(password: str) -> bool:
    """
    Checks if the password contains at least one digit.

    Arguments:
        password (str): The password to check.

    Returns:
        bool: True if there is at least one digit, otherwise False.
    """
    return any(char.isdigit() for char in password)


def is_good_password(password: str) -> bool:
    """
    Checks if the password is good using the LBYL (Look Before You Leap)
    approach.

    A good password meets the following criteria:
    - At least 9 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit

    Arguments:
        password (str): The password to check.

    Returns:
        bool: True if the password meets all criteria, otherwise False.
    """
    if not is_sufficient_length(password):
        raise LengthError  # Password length is insufficient

    if not has_uppercase(password) or not has_lowercase(password):
        raise LetterError  # Missing an uppercase or lowercase letter

    if not has_digit(password):
        raise DigitError  # Missing a digit

    return True  # All conditions are met
