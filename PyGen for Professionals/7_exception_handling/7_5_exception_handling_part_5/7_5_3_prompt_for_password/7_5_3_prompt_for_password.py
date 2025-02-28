'''
TODO:
    Let's call a password good if:
        - its length is 9 or more characters
        - it contains upper and lower case letters of any alphabet
        - it contains at least one digit

    Write a program that requires entering a new password until a good one
    is entered.

    Input data format:
        The program is given an arbitrary number of passwords, each on a
        separate line. It is guaranteed that there is a good one
        among them.

    Output data format:
        For each password entered, the program should output the text:
            - LengthError, if the length of the entered password is less
            than 9 characters
            - LetterError, if all the letters in it have the same case or
            are missing
            - DigitError, if there are no digits in it
            - Success!, if the entered password is good

    After entering a good password, all subsequent passwords should
    be ignored.

NOTE:
    The priority of the error message output in case of failure of several
    conditions is LengthError, then LetterError, and then DigitError.
'''


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
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


def validate_password(password: str):
    """
    Validates the password based on specific criteria:
    - Length is 9 or more characters
    - Contains both uppercase and lowercase letters
    - Contains at least one digit

    Raises:
        LengthError: If password is less than 9 characters long.
        LetterError: If password has no letters or all letters have the
                     same case.
        DigitError: If password has no digits.
    """
    if not is_sufficient_length(password):
        raise LengthError("Password must be at least 9 characters long.")

    if not has_uppercase(password) or not has_lowercase(password):
        raise LetterError(
            "Password must contain both uppercase and lowercase letters."
        )

    if not has_digit(password):
        raise DigitError("Password must contain at least one digit.")


def prompt_for_password():
    """
    Continuously prompts the user for a password until a valid one is entered.

    Output:
        Prints error message for invalid passwords and 'Success!'
        for the valid one.
    """
    while True:
        password = input("Enter password: ")

        try:
            validate_password(password)
        except LengthError:
            print("LengthError")
        except LetterError:
            print("LetterError")
        except DigitError:
            print("DigitError")
        else:
            print("Success!")
            break


# Run the password prompt function
prompt_for_password()
