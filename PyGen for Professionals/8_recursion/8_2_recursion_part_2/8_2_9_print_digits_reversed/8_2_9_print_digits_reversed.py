'''
TODO:
    Implement a print_digits() function using recursion that takes
    one argument:
        number — a natural number

    The function should print all the digits of number, starting with the most
    significant digits, each on a separate line.
'''


def print_digits(number: int) -> None:
    """
    Prints all the digits of the given number, starting with the most
    significant digit, each on a separate line.

    Args:
        number (int): A natural number.

    Returns:
        None: This function does not return a value.
    """
    if number >= 10:
        # Recursively call with the remaining digits until it's a single digit
        print_digits(number // 10)

    # Print the current most significant digit
    print(number % 10)


# Test the function
print_digits(12345)
