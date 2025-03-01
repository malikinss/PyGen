'''
TODO:
    Implement the is_power() function using recursion that takes one argument:
        number - is a natural number

    The function should return True if number is a power of 2, or
    False otherwise.
'''


def is_power(number: int) -> bool:
    """
    Determine if a number is a power of 2.

    Args:
        number (int): A natural number to be checked.

    Returns:
        bool: True if number is a power of 2, False otherwise.
    """
    # Base cases: 1 and 2 are powers of 2
    if number in (1, 2):
        return True

    # If the number is not divisible by 2, it's not a power of 2
    elif number % 2 != 0:
        return False

    # Recursively check if the number divided by 2 is a power of 2
    return is_power(number // 2)
