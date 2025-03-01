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
    # Edge case: If the number is less than or equal to 0,
    # it's not a power of 2.
    if number <= 0:
        return False

    # Base case: If the number is 1, it is a power of 2 (2^0 = 1).
    if number == 1:
        return True

    # If the number is divisible by 2, recursively check if the result
    # is a power of 2.
    if number % 2 == 0:
        return is_power(number // 2)

    # If none of the conditions match, it's not a power of 2.
    return False


# Test cases
print(is_power(16))  # True, 2^4 = 16
print(is_power(18))  # False, not a power of 2
print(is_power(1))   # True, 2^0 = 1
print(is_power(0))   # False, 0 is not a power of 2
print(is_power(-8))  # False, negative numbers can't be powers of 2
