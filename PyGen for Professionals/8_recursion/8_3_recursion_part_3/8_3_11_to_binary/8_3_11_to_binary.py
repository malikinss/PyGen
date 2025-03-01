'''
TODO:
    Implement a to_binary() function using recursion that takes one argument:
        - number is a non-negative integer

    The function should return a string representation of number in binary
    notation.
'''


def to_binary(number: int) -> str:
    """
    Convert a non-negative integer to its binary representation using
    recursion.

    Args:
        number (int): A non-negative integer.

    Returns:
        str: A string representing the binary notation of the input number.
    """
    if number in (0, 1):
        return str(number)

    # Recursively divide the number by 2 and concatenate the remainder.
    return to_binary(number // 2) + str(number % 2)
