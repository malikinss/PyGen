'''
TODO:
    Write a program that determines the number of days in a given month.

    The input to the program is the year and the serial number of the month
    (starting from 1), separated by a space.

    The program should output a single number - the number of days in
    the entered month.

NOTE:
    January has a serial number of 1, February - 2, March - 3, and so on.
'''
import calendar


def print_days_in_month(user_input):
    """
    Prints the number of days in the given month of a specified year.

    Args:
        user_input (str): A string containing the year and month number
                          separated by a space.

    Raises:
        ValueError: If the input format is incorrect or values are out
                    of range.
    """
    try:
        given_year, given_month = map(int, user_input.split())
        print(calendar.monthrange(given_year, given_month)[1])
    except ValueError:
        print("Invalid input. Please enter a valid year and month number.")


user_input = input("Enter year and month number (e.g., '2024 2'): ")
print_days_in_month(user_input)
