'''
TODO:
    Implement a print_digits() function using recursion that takes
    one argument:
        number — a natural number

    The function should print all the digits of number, starting with the
    least significant digits, each on a separate line.
'''


def print_digits(number: int) -> None:
    """
    Prints all the digits of the given number, starting with the least
    significant digit, each on a separate line.

    Args:
        number (int): A natural number.

    Returns:
        None: This function does not return a value.
    """
    if number > 0:
        print(number % 10)  # Print the least significant digit
        # Recursively call with the remaining number
        print_digits(number // 10)


# Test the function
print_digits(12345)
