'''
TODO:
        Implement the get_digits() function using type annotations that takes
        one argument:
        number is a positive integer or float number

        The function should return a list consisting of the digits of number.

NOTE:
        Use built-in types (list, tuple, ...), not types from the
        typing module.

        Also use the | notation, not the Union type from the typing module.

        The order of the digits in the list must match the order of their
        occurrence in the original number.
'''


def get_digits(number: int | float) -> list[int]:
    """
    Extract digits from a given positive integer or float.

    Args:
        number (int | float): The positive number from which to extract digits.

    Returns:
        list[int]: A list containing the digits of the number.
    """

    if number < 0:
        raise ValueError("Number must be positive")

    result = [int(digit) for digit in str(number) if digit.isdigit()]

    return result
