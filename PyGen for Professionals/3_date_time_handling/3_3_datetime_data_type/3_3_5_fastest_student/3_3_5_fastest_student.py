'''
TODO:
    Students at the BEEGEEK online school decided to find out which of them
    could solve their math homework the fastest.

    To do this, each student recorded the start and end time of solving
    their homework.

    You have access to a data dictionary containing student results.

    The key in the dictionary is the name of the student, and the value is
    a tuple, the first element of which is the start time of the solution,
    the second element is the end time of the solution.

    Complete the code below to display the name of the student who spent the
    least amount of time solving the homework problem.

NOTE:
    It is guaranteed that the required student is unique.

    Date-times in tuples are presented as strings in the format:
        DD.MM.YYYY HH:MM:SS

'''
from datetime import datetime


def convert_to_datetime(given_date: str) -> datetime | None:
    """
    Convert a date-time string in the format 'DD.MM.YYYY HH:MM:SS' to
    a datetime object.

    Args:
        given_date (str): A string representing the date and time in the
                          format: 'DD.MM.YYYY HH:MM:SS'.

    Returns:
        datetime: The corresponding datetime object.

    Raises:
        ValueError: If the provided date string doesn't match the expected
                    format.
    """
    try:
        return datetime.strptime(given_date, '%d.%m.%Y %H:%M:%S')
    except ValueError:
        print(f"Error: Invalid date-time format - {given_date}")
        return None


def fastest_student(data: dict[str, tuple[str, str]]) -> str:
    """
    Determines which student solved the homework the fastest by comparing the
    time spent solving the homework.

    The time spent is calculated as the difference between the start and end
    times recorded for each student.

    Args:
        data (dict[str, tuple[str, str]]): A dictionary where the keys are
                                           student names (str), and the values
                                           are tuples of start time and end
                                           time as strings in the format
                                           'DD.MM.YYYY HH:MM:SS'.

    Returns:
        str: The name of the student who spent the least time solving their
             homework.
        If no valid student can be found, returns an empty string.
    """
    min_time = float('inf')  # Initialize with a large number
    fastest_student_name = ''

    for name, (start_time, end_time) in data.items():
        # Convert start and end times to datetime
        start_time_dt = convert_to_datetime(start_time)
        end_time_dt = convert_to_datetime(end_time)

        # If both conversions were successful, calculate time spent
        if start_time_dt and end_time_dt:
            time_spent = (end_time_dt - start_time_dt).total_seconds()

            # Update the fastest student if this student took less time
            if time_spent < min_time:
                min_time = time_spent
                fastest_student_name = name

    return fastest_student_name


# Example data
data: dict[str, tuple[str, str]] = {
    'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
    'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
    'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
    'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
    'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
    'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
    'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
    'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
    'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
    'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
    'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')
}

# Find the fastest student
result = fastest_student(data)

# Print the result
if result:
    print(result)
