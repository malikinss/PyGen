'''
TODO:
        Let's call a password good if:
            - its length is 9 or more characters
            - it contains upper and lower case letters of any alphabet
            - it contains at least one digit

        Implement the is_good_password() function in LBYL style, which takes
        one argument:
            string — an arbitrary string

        The function should return True if the string is a good password, or
        False otherwise.
'''


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
    # Explicitly check conditions before making the final decision
    if not isinstance(password, str):
        return False  # Not a valid string

    if not is_sufficient_length(password):
        return False  # Password length is insufficient

    if not has_uppercase(password):
        return False  # Missing an uppercase letter

    if not has_lowercase(password):
        return False  # Missing a lowercase letter

    if not has_digit(password):
        return False  # Missing a digit

    return True  # All conditions are met
