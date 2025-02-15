'''
TODO:
    Write a program that displays a calendar for a given year and month.

    The input to the program is the year and the abbreviated name of the month
    in English, separated by a space.

    The program should display a calendar for the entered year and month.
'''
import calendar


def print_calendar():
    """
    Prompts the user to enter a year and an abbreviated month name,
    then displays the corresponding calendar.

    The input should be in the format: 'YYYY MMM' (e.g., '2024 Jan').
    """
    user_input = input(
        "Insert year and month name abbreviation (e.g., '2024 Jan'): "
    ).split()

    if len(user_input) != 2:
        print(
            "Error: ",
            "Please enter the year and month abbreviation separated by a ' '."
        )
        return

    try:
        given_year = int(user_input[0])
    except ValueError:
        print("Error: Invalid year. Please enter a numeric year.")
        return

    if user_input[1] not in calendar.month_abbr:
        print("Error: Wrong month name abbreviation.")
        return

    given_month = calendar.month_abbr.index(user_input[1])
    calendar.prmonth(given_year, given_month)


print_calendar()
