'''
TODO:
    Given a natural number.

    Write a program that prints its digits in a column in reverse order.
'''


def print_digits_reverse(n: int):
    """
    Prints the digits of the given natural number in reverse order,
    each on a new line.

    Args:
        n (int): The natural number whose digits will be printed in reverse.
    """
    while n != 0:
        last_digit = n % 10  # Get the last digit of the number
        n = n // 10  # Remove the last digit from the number
        print(last_digit)  # Print the last digit


# Input
num = int(input("Enter a natural number: "))

# Call the function
print_digits_reverse(num)
