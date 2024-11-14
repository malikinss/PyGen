'''
TODO:
    Given a natural number n, (n>9).

    Write a program that determines its second (from the beginning) digit.
'''


def second_digit(n: int) -> int:
    """
    Given a natural number n (n > 9), this function returns its second digit
    (from the left).

    Args:
        n (int): The input natural number.

    Returns:
        int: The second digit of the number.
    """
    # Use a while loop to reduce the number until it has exactly two digits
    while n >= 100:
        n //= 10

    # Extract the second digit
    # (the first digit of the remaining two-digit number)
    return n % 10


# Example usage:
n = int(input())
print(second_digit(n))
