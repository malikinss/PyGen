'''
TODO:
    Write a program using recursion that takes a number as input and outputs
    the sum of the digits of that number.
'''


def get_digits_sum(number: int) -> int:
    """
    Calculate the sum of the digits of a given number using recursion.

    Args:
        number (int): The number whose digits sum is to be calculated.

    Returns:
        int: The sum of the digits of the input number.
    """
    # Base case: if the number is a single digit, return it
    if 0 <= number < 10:
        return number

    # Recursive case: add the last digit to the sum of the remaining digits
    return number % 10 + get_digits_sum(number // 10)


# Test the function
print(get_digits_sum(111211))  # Output should be 7 (1+1+1+2+1+1)
