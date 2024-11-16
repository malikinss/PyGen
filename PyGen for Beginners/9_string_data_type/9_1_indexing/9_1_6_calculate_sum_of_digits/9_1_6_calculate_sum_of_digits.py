'''
TODO:
    The input to the program is one string consisting of numbers.

    Write a program that calculates the sum of the digits in a given string.
'''


def calculate_sum_of_digits(number_string: str) -> int:
    """
    Calculates the sum of digits in the given string containing numbers.

    Args:
        number_string (str): A string consisting of numeric characters.

    Returns:
        int: The sum of all digits in the string.
    """
    total_sum = 0
    for char in number_string:
        total_sum += int(char)
    return total_sum


# User input
given_string = input("Enter a string of numbers: ")

# Output result
result = calculate_sum_of_digits(given_string)
print(result)
