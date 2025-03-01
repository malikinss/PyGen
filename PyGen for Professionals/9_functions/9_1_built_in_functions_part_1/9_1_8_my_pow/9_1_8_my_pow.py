"""
TODO:
    Implement a function sum_of_powers_of_digits() that takes one argument:
        number — a non-negative integer

    The function should return a sum consisting of the digits of the number
    raised to the power of their ordinal number.

NOTE:
    Consider the number 139 from the first test.

    The sum of the digits of this number raised to the power of their ordinal
    number is:
        1^1 + 3^2 + 9 ^ 3 = 739

    It is convenient to use the enumerate() and sum() functions in the problem.
"""


def sum_of_powers_of_digits(number: int) -> int:
    """
    Calculate the sum of digits each raised to the power of their position.

    Args:
        number (int): A non-negative integer.

    Returns:
        int: The sum of digits raised to the power of their respective
        positions.
    """
    if number < 0:
        raise ValueError("The number must be a non-negative integer.")

    digits = enumerate(str(number), start=1)

    return sum(int(digit) ** exponent for exponent, digit in digits)


# Test case
# Expected output: 739 (1^1 + 3^2 + 9^3)
print(sum_of_powers_of_digits(139))
