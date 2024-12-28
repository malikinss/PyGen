'''
TODO:
    A magic date is the date when the day multiplied by the month equals
    the number formed by the last two digits of the year.

    Write a function is_magic(date) that takes a string representation
    of a valid date as an argument and returns True if the date is magic
    and False otherwise.
'''


def is_magic(date: str) -> bool:
    """
    Checks if a given date is a magic date.

    A magic date is when the day multiplied by the month equals
    the last two digits of the year.

    Args:
        date (str): A string representing the date in the format "DD.MM.YYYY".

    Returns:
        bool: True if the date is magic, False otherwise.
    """
    # Split the input date string into day, month, and year
    seq = date.split(".")
    day, month, year = int(seq[0]), int(seq[1]), int(seq[2])

    # Check if the date is magic
    return day * month == year % 100


# Input
date = input("Enter date in DD.MM.YYYY format: ")

# Output
print(is_magic(date))
