'''
TODO:
    Given a natural number.

    Write a program that reverses the order of the digits of a number.
'''


def reverse_number(n: int) -> int:
    """
    Reverses the digits of a given natural number.

    Args:
        n (int): The number to reverse.

    Returns:
        int: The reversed number.
    """
    reversed_num = 0
    while n != 0:
        last_digit = n % 10  # Get the last digit
        reversed_num = reversed_num * 10 + last_digit  # Add last digit
        n //= 10  # Remove the last digit from the original number
    return reversed_num


# Input
num = int(input("Enter a natural number: "))

# Output
print(reverse_number(num))
