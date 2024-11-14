'''
TODO:
    Given a natural number.

    Write a program that determines if a given number consists
    of the same digits.
'''


def has_same_digits(n: int) -> str:
    """
    This function checks if a given natural number consists of the same digits.

    Args:
        n (int): The input natural number.

    Returns:
        str: "YES" if the number consists of the same digits, otherwise "NO".
    """
    last_digit = n % 10  # Get the last digit of the number

    while n > 0:
        cur_digit = n % 10  # Get the current digit
        if last_digit != cur_digit:
            return "NO"
        n //= 10  # Remove the last digit from the number

    return "YES"


# Example usage:
n = int(input())
print(has_same_digits(n))
