'''
TODO:
    Write a program that determines the number of days in a given month.

    The input to the program is the year and the full name of the month
    in English, separated by a space.

    The program should output a single number - the number of days in
    the entered month.
'''
import calendar


def print_days_in_month_by_name(user_input):
    """
    Prints the number of days in the given month of a specified year.

    Args:
        user_input (str): A string containing the year and the full name of
                          the month separated by a space.

    Raises:
        ValueError: If the input format is incorrect or the month name
                    is invalid.
    """
    try:
        given_data = user_input.split()

        given_year = int(given_data[0])
        given_month_name = given_data[1].capitalize()

        english_month_names = list(calendar.month_name)

        # Check if the month name is valid
        if given_month_name not in english_month_names:
            print(
                f"Invalid month name: '{given_month_name}'.",
                "Please enter a valid month."
            )
            return

        given_month_num = english_month_names.index(given_month_name)

        _, number_of_days = calendar.monthrange(given_year, given_month_num)

        print(number_of_days)

    except ValueError:
        print("Invalid input. Please enter a valid year and month name.")


user_input = input("Enter year and month name (e.g., '2024 February'): ")
print_days_in_month_by_name(user_input)
