'''
TODO:
    Write a function is_password_good(password) that takes the string value
    password as an argument and returns True if the password is strong
    and False otherwise.

    A password is strong if:
        - its length is at least 8 characters;
        - it contains at least one capital letter (upper case);
        - it contains at least one lowercase letter (lower case);
        - it contains at least one digit.
'''


def is_password_good(password):
    """
    Checks if the given password is strong.

    A strong password must meet the following criteria:
        - It has at least 8 characters.
        - It contains at least one uppercase letter.
        - It contains at least one lowercase letter.
        - It contains at least one digit.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password is strong, False otherwise.
    """
    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) < 8:
        return False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit


# Example usage
txt = input("Enter password: ")
print(is_password_good(txt))
