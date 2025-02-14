'''
TODO:
    Write a program that determines whether a year is a leap year.

    The input to the program in the first line is an integer n, in the next n
    lines natural numbers representing years are entered.

    For each year entered, the program must print True if it is a leap year,
    or False otherwise.
'''
import calendar


def is_valid_integer(value):
    """
    Validates if the given value is an integer.

    Args:
        value (str): The input value as a string.

    Returns:
        int: The converted integer if valid, otherwise None.
    """
    try:
        return int(value)
    except ValueError:
        return None


def check_leap_years():
    """
    Determines whether given years are leap years.

    The user is prompted to enter the number of years and then the years
    themselves.

    The program prints True for a leap year and False otherwise.
    """
    num_years = is_valid_integer(input("Enter the number of years: "))

    if num_years is None or num_years <= 0:
        print(
            "Invalid input.",
            "Please enter a valid positive integer for the number of years."
        )
        return

    for _ in range(num_years):
        while True:
            given_year = is_valid_integer(input("Enter year: "))

            if given_year is not None and given_year > 0:
                print(calendar.isleap(given_year))
                break

            print(
                "Invalid input.",
                "Please enter a valid positive integer for the year."
            )


check_leap_years()
