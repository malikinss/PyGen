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
        # Base case: if number is 0 or 1, return it as a string.
        return str(number)

    # Recursively call to_binary with number // 2 (integer division by 2),
    # and append the remainder of number % 2 to form the binary representation.
    return to_binary(number // 2) + str(number % 2)


# Example usage
print(to_binary(5))  # Output: '101'
print(to_binary(10))    # Output: '1010'
print(to_binary(0))  # Output: '0'
print(to_binary(1))  # Output: '1'
