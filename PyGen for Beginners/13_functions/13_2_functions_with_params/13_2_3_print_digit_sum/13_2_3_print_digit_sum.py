'''
TODO:
    Write a print_digit_sum() function that takes a single integer num and
    prints the sum of its digits.
'''


def print_digit_sum(num: int) -> None:
    """
    Prints the sum of the digits of the given number.

    The function takes an integer `num`, calculates the sum of its digits,
    and prints the result.

    Args:
    num (int): The integer whose digits' sum is to be calculated.

    Returns:
    None
    """
    digit_sum = 0

    # Calculate the sum of digits
    while num > 0:
        digit_sum += num % 10
        num //= 10

    # Print the result
    print(digit_sum)


# Example usage
n = int(input())  # Read input
print_digit_sum(n)  # Call the function
