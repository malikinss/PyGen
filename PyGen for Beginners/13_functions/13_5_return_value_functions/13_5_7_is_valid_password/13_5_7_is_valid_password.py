'''
TODO:
    BEEGEEK has finally opened its own bank, which uses special ATMs with
    an unusual password.

    A valid BEEGEEK bank password is a:b:c, where a, b and c are
    natural numbers.

    Since the founder of BEEGEEK is a math fanatic, he decided:
        number a - must be a palindrome;
        number b - must be prime;
        number c - must be even.

    Write a function is_valid_password(password) that takes the string value
    of password as an argument and returns True if the password is a valid
    BEEGEEK bank password and False otherwise.
'''


def is_palindrome(text: str) -> bool:
    """
    Checks if the given text is a palindrome.

    Args:
        text (str): The text to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    # Remove unwanted symbols and make the string lowercase
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')

    text = text.lower()
    return text == text[::-1]


def is_even(num: int) -> bool:
    """
    Checks if a number is even.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return num % 2 == 0


def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_valid_password(password: str) -> bool:
    """
    Validates a BEEGEEK bank password.

    A valid password follows the format a:b:c where:
        - a is a palindrome,
        - b is prime,
        - c is even.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    seq = password.split(":")

    if len(seq) == 3:
        try:
            a, b, c = map(int, seq)
            return is_palindrome(str(a)) and is_prime(b) and is_even(c)
        except ValueError:
            return False  # If conversion fails, return False

    return False


# Example usage
psw = input("Enter password: ")
print(is_valid_password(psw))
