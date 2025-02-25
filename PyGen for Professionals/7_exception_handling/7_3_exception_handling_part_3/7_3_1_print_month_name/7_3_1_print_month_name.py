'''
TODO:
    Write a program using the try-except construct that outputs the name
    of the month corresponding to the entered integer (from 1 to 12
    inclusive), and if the entered number does not belong to the interval
    [1;12], the program should output the text:
        The entered number is from an invalid range

    If the entered value isnt an integer, program should output the text:
        The entered value is incorrect

    The program receives a single line with an arbitrary value as input.

    The program should output the full name of the month in English
    corresponding to the entered number (from 1 to 12 inclusive) or the
    text with the corresponding error if the entered value is incorrect.

NOTE:
    To get a list of month names, recall the month_name attribute from the
    calendar module.
'''
from calendar import month_name


def print_month_name() -> None:
    """
    Reads an integer from input and prints the corresponding month name.
    If the input is not an integer or is out of range, prints an error message.
    """
    months = {key: month_name[key] for key in range(1, 13)}

    try:
        month_number = int(input())
        try:
            print(months[month_number])
        except KeyError:
            print('The entered number is from an invalid range')
    except ValueError:
        print('The entered value is incorrect')


print_month_name()
