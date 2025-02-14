'''
TODO:
    Arthur needs to prepare 10 problems for the new course "OOP in Python".

    To prevent the task from being tedious, he came up with a rule:
        - if today he prepared the first task, then he should prepare
          the second in one day
        - if today he prepared the second task, then he should prepare
          the third in two days
        - if today he prepared the third task, then he must prepare the fourth
          in three days, and so on

    Write a program that determines the dates on which Arthur needs to prepare
    tasks.
'''
from datetime import datetime, timedelta

DATE_FORMAT = '%d.%m.%Y'
TASKS_COUNT = 10  # Number of tasks


def get_user_date() -> datetime:
    """
    Prompts the user to input a date and returns it as a datetime object.

    Returns:
        datetime: The user-provided date.
    """
    while True:
        user_input = input(
            'Enter a date in the format DD.MM.YYYY (e.g., 01.01.1995): '
        )
        try:
            return datetime.strptime(user_input, DATE_FORMAT)
        except ValueError:
            print('Error: Invalid date format. Please try again.')


def calculate_task_dates(
    start_date: datetime, num_tasks: int = TASKS_COUNT
) -> list[datetime]:
    """
    Calculates the preparation dates for the tasks.

    Args:
        start_date (datetime): The start date.
        num_tasks (int): Number of tasks (default is 10).

    Returns:
        list[datetime]: List of task preparation dates.
    """
    return [
        start_date + timedelta(days=sum(range(1, i + 1)))
        for i in range(1, num_tasks + 1)
    ]


def display_dates(dates: list[datetime]) -> None:
    """
    Displays the list of dates in DD.MM.YYYY format.

    Args:
        dates (list[datetime]): The list of dates to display.
    """
    print('\n'.join(date.strftime(DATE_FORMAT) for date in dates))


start_date = get_user_date()
task_dates = calculate_task_dates(start_date)
display_dates(task_dates)
