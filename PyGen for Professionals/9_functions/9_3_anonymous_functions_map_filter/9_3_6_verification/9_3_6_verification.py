'''
TODO:
        Implement the verification() function, which checks the correctness of
        the entered password.

        It must accept four arguments in the following order:
            login — user login
            password — user password
            success — some function
            failure — some function

        A password is considered correct if it contains at least one uppercase
        Latin letter, at least one lowercase Latin letter, and at least
        one digit.

        The verification() function must call the success() function with the
        login argument if the passed password is correct, otherwise
        the failure() function with the login arguments and an error
        message string:
            - the password does not contain any letters, if the password does
            not contain Latin letters
            - the password does not contain any uppercase letters, if the
            password does not contain uppercase Latin letters
            - the password does not contain any lowercase letters, if the
            password does not contain lowercase Latin letters
            - the password does not contain any digits, if the password does
            not contain digits

NOTE:
        If the password does not satisfy several conditions, the error message
        string selection priorities are as follows:
            - the password does not contain any letters
            - the password does not contain any uppercase letters
            - the password does not contain any lowercase letters
            - the password does not contain any digits
'''
from typing import Callable
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits


def verification(login: str,
                 password: str,
                 success: Callable[[str], None],
                 failure: Callable[[str, str], None]) -> None:
    """
    Checks the correctness of the entered password.

    Args:
        login (str): User login
        password (str): User password
        success (Callable[[str], None]): Function to call if the password
        is correct
        failure (Callable[[str, str], None]): Function to call if the password
        is incorrect

    Returns:
        None
    """
    # Define conditions and their corresponding error messages
    def check_condition(password: str, condition: str) -> bool:
        """
        Check if the password contains at least one character from the
        condition set.

        Args:
            password (str): The password to check.
            condition (str): The set of characters to check against.

        Returns:
            bool: True if condition is met, False otherwise.
        """
        return any(char in condition for char in password)

    # Password condition checks with error messages
    password_checks = [
        (lambda pwd: check_condition(pwd, ascii_letters), 'в пароле нет ни одной буквы'),
        (lambda pwd: check_condition(pwd, ascii_uppercase), 'в пароле нет ни одной заглавной буквы'),
        (lambda pwd: check_condition(pwd, ascii_lowercase), 'в пароле нет ни одной строчной буквы'),
        (lambda pwd: check_condition(pwd, digits), 'в пароле нет ни одной цифры')
    ]

    # Check each condition in order of priority
    for condition, error_message in password_checks:
        if not condition(password):
            failure(login, error_message)
            return

    # If all conditions are met, call the success function
    success(login)
