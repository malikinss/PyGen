'''
TODO:
    A good password according to the conditions of this problem consists of at
    least 7 characters, contains at least one digit, uppercase and lowercase
    letter.

    Write a program with a built-in any() function to determine whether the
    entered password is good.
'''


def is_password_strong(password: str) -> bool:
    """
    Checks whether a password meets the required strength criteria:
    - At least 7 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password is strong, False otherwise.
    """
    return (
        len(password) >= 7
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
    )


# Read input and check password strength
print("YES" if is_password_strong(input()) else "NO")
