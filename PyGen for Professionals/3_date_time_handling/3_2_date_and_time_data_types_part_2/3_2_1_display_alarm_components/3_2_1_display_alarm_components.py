'''
TODO:
    Alarm time is available to you.

    Complete the code below to output the following components:
        number of hours in HH format
        number of minutes in MM format
        number of seconds in SS format
'''
from datetime import time


def print_alarm_components(alarm_time: time) -> None:
    """
    Prints the hours, minutes, and seconds from the given alarm time.

    Args:
        alarm_time (time): The time object representing the alarm time.
    """
    print(f'Hours: {alarm_time.strftime("%H")}')
    print(f'Minutes: {alarm_time.strftime("%M")}')
    print(f'Seconds: {alarm_time.strftime("%S")}')


# Example usage
alarm = time(7, 30, 25)
print_alarm_components(alarm)
