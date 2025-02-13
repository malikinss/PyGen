'''
TODO:
    Write a program that takes a sequence of dates as input and checks each of
    them for correctness.

    The input to the program is a sequence of dates in the format DD.MM.YYYY,
    each on a separate line. The end of the sequence is the word end.

    For each date entered, the program should display the text Correct or
    Incorrect, depending on whether the date is correct, and then display the
    number of correct dates.

NOTE:
    To analyze the date for correctness, you can use the already implemented
    is_correct() function from the previous task.
'''
from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    """
    Checks if the given day, month, and year form a valid date.

    Args:
        day (int): The day of the month.
        month (int): The month of the year.
        year (int): The year.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


def check_correct_dates() -> None:
    """
    Reads a sequence of dates from user input, checks their validity,
    and counts the number of correct dates.

    Input format:
        - Dates should be entered in the format DD.MM.YYYY, each on a new line.
        - The input sequence ends with the word "end".

    Output:
        - "Correct" if the date is valid.
        - "Incorrect" if the date is invalid.
        - The total count of valid dates.
    """
    correct_dates_counter = 0

    while True:
        user_input = input().strip()

        if user_input.lower() == "end":
            break

        try:
            day, month, year = map(int, user_input.split('.'))
            if is_correct(day, month, year):
                print("Correct")
                correct_dates_counter += 1
            else:
                print("Incorrect")
        except ValueError:
            # Handles cases where input isn't in the correct format
            print("Incorrect")

    print(correct_dates_counter)
