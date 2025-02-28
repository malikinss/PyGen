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
    # Check if the length is sufficient before proceeding
    if len(password) < 9:
        return False  # Password length is insufficient

    # Check if it contains both uppercase and lowercase letters
    has_upper = False
    has_lower = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        if has_upper and has_lower:
            break  # No need to continue checking once both are found

    # If either uppercase or lowercase is missing
    if not has_upper or not has_lower:
        return False

    # Check if it contains at least one digit
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False

    # If all checks pass, return True
    return True
