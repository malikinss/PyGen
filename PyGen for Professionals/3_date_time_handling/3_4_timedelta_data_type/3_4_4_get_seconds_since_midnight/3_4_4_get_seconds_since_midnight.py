'''
TODO:
    Write a program that takes time as input and outputs the integer number of
    seconds that have passed since the beginning of the day.

NOTE:
    The beginning of the day is considered to be the moment in time
    corresponding to 00:00:00
'''
from datetime import datetime

TIME_FORMAT = "%H:%M:%S"


def get_seconds_since_midnight(time_str: str) -> int:
    """
    Calculates the number of seconds that have passed since the beginning\
    of the day.

    Args:
        time_str (str): A time string in the format "HH:MM:SS".

    Returns:
        int: The number of seconds since midnight (00:00:00).
    """
    current_time = datetime.strptime(time_str, TIME_FORMAT)
    secs_in_hours = current_time.hour * 3600
    secs_in_minutes = current_time.minute * 60

    seconds_since_midnight = (
        secs_in_hours + secs_in_minutes + current_time.second
    )

    return seconds_since_midnight


# Example usage
user_time = input("Please input the time in the format HH:MM:SS: ")
print(get_seconds_since_midnight(user_time))
