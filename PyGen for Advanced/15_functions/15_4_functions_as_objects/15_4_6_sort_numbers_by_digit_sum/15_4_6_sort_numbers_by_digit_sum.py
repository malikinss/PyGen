'''
TODO:
    The program is given a string of natural numbers as input.

    A list of numbers is formed from the elements of the string.

    Write a program to sort a list of numbers in non-decreasing order of the
    sum of their digits.

    In this case, if two numbers have the same sum of digits, their relative
    positions in the initial list should be preserved.
'''


def get_sum_of_digits(number_as_string: str) -> int:
    """
    Returns the sum of the digits of the given number string.

    Args:
        number_as_string (str): The number as a string.

    Returns:
        int: The sum of the digits of the number.
    """
    return sum(int(digit) for digit in number_as_string)


def sort_numbers_by_digit_sum(numbers_as_string_list: list) -> list:
    """
    Sorts the list of numbers by the sum of their digits in non-decreasing
    order.

    Args:
        numbers_as_string_list (list): A list of numbers as strings.

    Returns:
        list: A list of numbers sorted by the sum of their digits.
    """
    return sorted(numbers_as_string_list, key=get_sum_of_digits)


# Example usage:
numbers_as_string_list = input("Enter the list of numbers: ").split()
sorted_numbers = sort_numbers_by_digit_sum(numbers_as_string_list)
print(*sorted_numbers)
