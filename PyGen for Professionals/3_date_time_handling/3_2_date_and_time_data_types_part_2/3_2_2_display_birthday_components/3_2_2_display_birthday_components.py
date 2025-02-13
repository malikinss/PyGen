'''
TODO:
    The birthday date is available to you.

    Complete the code below to output the following components:
        - full name of the month in English
        - full name of the day of the week in English
        - year in YYYY format
        - month number in MM format
        - day of the month in DD format
'''
from datetime import date


def print_birthday_components(birthday: date) -> None:
    """
    Prints the components of a given birthday date in various formats.

    Args:
        birthday (date): The date object representing the birthday.
    """
    print('Name of the month:', birthday.strftime('%B'))
    print('Name of the weekday:', birthday.strftime('%A'))
    print('Year:', birthday.strftime('%Y'))
    print('Month:', birthday.strftime('%m'))
    print('Day:', birthday.strftime('%d'))


# Example usage
birthday = date(1992, 10, 6)
print_birthday_components(birthday)
