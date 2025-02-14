'''
TODO:
    While solving the next problem, the programmer records the start and end
    times of its solution and adds the results obtained to the data list.

    Each result is a tuple, the first element of which is the start time of
    the solution as a string in the HH:MM format, the second element is the
    end time of the solution as a string in the same format.

    Complete the code below to print the total integer number of minutes the
    programmer spent solving all problems.
'''

from datetime import datetime, timedelta
from typing import List, Tuple

TIME_FORMAT = '%H:%M'


def parse_time(string_time: str) -> datetime:
    """
    Converts a time string in HH:MM format to a datetime object.

    Args:
        string_time (str): Time string in HH:MM format.

    Returns:
        datetime: Corresponding datetime object.
    """
    return datetime.strptime(string_time, TIME_FORMAT)


def calculate_task_duration(task: Tuple[str, str]) -> timedelta:
    """
    Calculates the duration of a single task.

    Args:
        task (Tuple[str, str]): Tuple containing start and end times.

    Returns:
        timedelta: Duration of the task.
    """
    start_time, end_time = map(parse_time, task)

    if end_time < start_time:
        raise ValueError('End time cannot be before start time.')

    return end_time - start_time


def calculate_total_duration(data: List[Tuple[str, str]]) -> int | float:
    """
    Calculates the total duration of all tasks in minutes.

    Args:
        data (List[Tuple[str, str]]): List of tuples containing start and
                                      end times.

    Returns:
        int: Total duration in minutes.
    """
    total_duration = sum(
        (calculate_task_duration(task) for task in data), timedelta()
    )
    return total_duration.total_seconds() // 60


# Task records
data = [
    ('07:14', '08:46'),
    ('09:01', '09:37'),
    ('10:00', '11:43'),
    ('12:13', '13:49'),
    ('15:00', '15:19'),
    ('15:58', '17:24'),
    ('17:57', '19:21'),
    ('19:30', '19:59')
]

# Print total minutes spent
print(int(calculate_total_duration(data)))
