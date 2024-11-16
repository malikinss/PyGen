'''
TODO:
    Given a natural number n, (n>99).

    Write a program that determines its third (from the beginning) digit.
'''


def third_digit(n: int) -> int:
    """
    Returns the third digit from the beginning of the given natural number n.

    Args:
        n (int): A natural number greater than 99.

    Returns:
        int: The third digit from the left of n.
    """
    while n >= 1000:
        n //= 10
    return n % 10


# Input and function call
n = int(input("Enter a number greater than 99: "))
print(third_digit(n))
