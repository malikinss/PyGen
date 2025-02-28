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


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(password: str) -> bool:
    """
    Checks if the password is good using the EAFP (Easier to Ask for
    Forgiveness than Permission) approach.

    A good password meets the following criteria:
    - At least 9 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit

    Arguments:
        password (str): The password to check.

    Returns:
        bool: True if the password meets all criteria.

    Raises:
        LengthError: If the password is less than 9 characters long.
        LetterError: If the password contains no letters or all letters have
                     the same case.
        DigitError: If the password contains no digits.
    """
    try:
        # Check if the password length is 9 or more
        if len(password) < 9:
            raise LengthError("Password must be at least 9 characters long.")

        # Check if the password contains both uppercase and lowercase letters
        if not any(
            char.isupper() for char in password
        ) or not any(
            char.islower() for char in password
        ):
            raise LetterError(
                "Password must contain both uppercase and lowercase letters."
            )

        # Check if the password contains at least one digit
        if not any(char.isdigit() for char in password):
            raise DigitError("Password must contain at least one digit.")

        return True

    except LengthError:
        raise  # Raise LengthError if password is too short
    except LetterError:
        raise  # Raise LetterError if uppercase or lowercase is missing
    except DigitError:
        raise  # Raise DigitError if no digits are found
