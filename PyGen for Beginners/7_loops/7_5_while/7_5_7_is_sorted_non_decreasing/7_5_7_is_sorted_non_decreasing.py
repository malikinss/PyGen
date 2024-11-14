'''
TODO:
    Given a natural number.

    Write a program that determines whether the sequence of its digits,
    when viewed from right to left, is sorted in non-decreasing order.

    The program should print "YES" if the sequence of its digits when
    viewed from right to left is in non-decreasing order and "NO" otherwise.
'''


def is_sorted_non_decreasing(n: int) -> str:
    """
    This function checks if the digits of the given natural number,
    when viewed from right to left, are sorted in non-decreasing order.

    Args:
        n (int): The input natural number.

    Returns:
        str: "YES" if the digits are sorted in non-decreasing order from right
             to left, otherwise "NO".
    """
    last_digit = n % 10  # Get the last digit
    n //= 10  # Remove the last digit

    while n > 0:
        current_digit = n % 10  # Get the current digit

        if current_digit > last_digit:
            return "NO"

        last_digit = current_digit  # Update last_digit for the next comparison
        n //= 10  # Remove the current digit

    return "YES"


# Example usage:
n = int(input())
print(is_sorted_non_decreasing(n))
