'''
TODO:
    Write a function get_days(month) that takes a month number as an argument
    and returns the number of days in a given month.

NOTE:
    It is guaranteed that the argument passed is in the range from 1 to 12.
    Consider the year to be a non-leap year.
'''


def get_days(month: int) -> int:
    """
    Returns the number of days in a given month.

    The function takes a month number (1 to 12) and returns the number of
    days in that month. It assumes that the year is a non-leap year.

    Args:
    month (int): The month number:
                    (1 for January, 2 for February, ..., 12 for December).

    Returns:
    int: The number of days in the specified month.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 28


# Example usage
num = int(input())  # Read input month number
print(get_days(num))  # Call the function and print the result
