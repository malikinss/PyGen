'''
TODO:
    A math tutor conducts lessons for 45 minutes with breaks of 10 minutes.

    The tutor indicates the start time of the working day and the end time of
    the working day.

    Write a program that generates and displays a class schedule.

NOTE:
    If a lesson is interrupted by the end time of work, then there is no need
    to add it to the schedule

    If the difference between the start and end times of the working day is
    less than 45 minutes, the program should not output anything.
'''
from datetime import datetime, timedelta

TIME_FORMAT = '%H:%M'

LESSON_DURATION = 45
BREAK_DURATION = 10


def get_time_from_string(time_str: str) -> datetime:
    """
    Convert a string time to a datetime object.

    Args:
        time_str (str): Time in HH:MM format.

    Returns:
        datetime: Corresponding datetime object.
    """
    try:
        return datetime.strptime(time_str, TIME_FORMAT)
    except ValueError:
        raise ValueError("Invalid time format. Please use the format HH:MM")


def get_string_from_time(time_obj: datetime) -> str:
    """
    Convert a datetime object to a string in HH:MM format.

    Args:
        time_obj (datetime): The datetime object.

    Returns:
        str: Time in HH:MM format.
    """
    return time_obj.strftime(TIME_FORMAT)


def calculate_schedule(start_time: datetime, end_time: datetime):
    """
    Calculate and return a list of lessons' start and end times.

    Args:
        start_time (datetime): The starting time of the workday.
        end_time (datetime): The ending time of the workday.

    Returns:
        List[str]: List of lessons in HH:MM - HH:MM format.
    """
    lessons = []
    current_time = start_time

    while current_time + timedelta(minutes=LESSON_DURATION) <= end_time:
        lesson_end_time = current_time + timedelta(minutes=LESSON_DURATION)
        current_time_str = get_string_from_time(current_time)
        lesson_end_time_str = get_string_from_time(lesson_end_time)

        lessons.append(f"{current_time_str} - {lesson_end_time_str}")
        current_time = lesson_end_time + timedelta(minutes=BREAK_DURATION)

    return lessons


def display_schedule():
    """
    Prompts the user to enter the start and end times of the workday,
    calculates the class schedule, and displays it if the workday is long
    enough for at least one lesson.

    If the workday is too short for a lesson, a message indicating that
    is displayed.
    """
    try:
        start_time_str = input("Enter start time (HH:MM): ")
        end_time_str = input("Enter end time (HH:MM): ")

        start_time = get_time_from_string(start_time_str)
        end_time = get_time_from_string(end_time_str)

        # Check if there is enough time for at least one lesson
        if (end_time - start_time).total_seconds() < LESSON_DURATION * 60:
            print("The workday is too short for even a single lesson.")
            return

        # Get the schedule and display it
        schedule = calculate_schedule(start_time, end_time)
        if schedule:
            print("\nClass schedule:")
            print("\n".join(schedule))

    except ValueError as e:
        print(e)


display_schedule()
