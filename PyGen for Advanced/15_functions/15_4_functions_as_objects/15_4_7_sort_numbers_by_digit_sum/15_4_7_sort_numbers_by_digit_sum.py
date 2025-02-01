'''
TODO:
    The program is given a string of natural numbers as input.

    A list of numbers is formed from the elements of the string.

    Write a program to sort a list of numbers in non-decreasing order of the
    sum of their digits.

    In this case, if two numbers have the same sum of digits, they should be
    output in non-decreasing order.
'''


def get_sum_of_digits(number_as_string: str) -> tuple:
    """
    Returns a tuple of the sum of digits and the number itself.

    Args:
        number_as_string (str): The number as a string.

    Returns:
        tuple: A tuple (sum of digits, original number as int)
    """
    total = sum(int(digit) for digit in number_as_string)
    return total, int(number_as_string)


def sort_numbers_by_digit_sum(numbers_as_string_list: list) -> list:
    """
    Sorts the list of numbers based on the sum of digits and then by the value
    itself.

    Args:
        numbers_as_string_list (list): List of numbers as strings.

    Returns:
        list: Sorted list of numbers as strings.
    """
    return sorted(numbers_as_string_list, key=get_sum_of_digits)


# Example usage
numbers_as_string_list = input("Enter a string of natural numbers: ").split()
sorted_numbers = sort_numbers_by_digit_sum(numbers_as_string_list)

# Print the sorted numbers in their original form (as strings)
print(*sorted_numbers)
