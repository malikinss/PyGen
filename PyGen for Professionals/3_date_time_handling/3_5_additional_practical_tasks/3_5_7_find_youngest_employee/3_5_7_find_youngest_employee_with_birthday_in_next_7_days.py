'''
TODO:
    A list of employees of the organization is given, which indicates their
    last names, given names and dates of birth.

    Write a program that determines the youngest employee who celebrates his
    birthday within the next seven days from the current date.

    The input to the program in the first line is the current date in the
    format DD.MM.YYYY, in the next line the natural number n is entered - the
    number of employees working in the organization.

    In the next n lines, data about each employee is entered: first name, last
    name and date of birth, separated by a space. Date of birth is indicated
    in the format DD.MM.YYYY.

    The program should determine the youngest employee celebrating his
    birthday within the next seven days, and display his first and last name,
    separated by a space.

    If there are no such employees, the program should output the text:
        'No birthdays planned'

NOTE:
    It is guaranteed that all employees have different dates of birth.
'''
from datetime import datetime, timedelta, date
from typing import Callable


DATE_FORMAT = '%d.%m.%Y'


def parse_date(date_string: str) -> date:
    """
    Parse a string into a date object.
    Args:
        date_string (str): Date in DD.MM.YYYY format.
    Returns:
        date: The parsed date object.
    """
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError(
            'Invalid datetime format. Please use the format DD.MM.YYYY'
        )


def collect_employees_data(employees_num: int) -> dict:
    """
    Collect employee data, including first name, last name, and birth date.
    Args:
        employees_num (int): Number of employees.
    Returns:
        dict: A dictionary with employee names as keys and birth dates
              as values.
    """
    employees = {}
    for _ in range(employees_num):
        employee_name, employee_lastname, birthday_str = input().split(' ')
        employee = f"{employee_name} {employee_lastname}"
        birthday_date = parse_date(birthday_str)
        employees[employee] = birthday_date
    return employees


def get_next_7_days(current_date: date) -> list:
    """
    Get a list of the next 7 days after the current date.
    Args:
        current_date (date): The current date.
    Returns:
        list: List of the next 7 days (date objects).
    """
    return [current_date + timedelta(days=i) for i in range(1, 8)]


def filter_employees_in_next_7_days(
    cur_date: date, employees_data: dict
) -> dict:
    """
    Filter employees who have birthdays within the next 7 days.
    Args:
        cur_date (date): The current date.
        employees_data (dict): Dictionary with employee names and birth dates.
    Returns:
        dict: A dictionary of employees with birthdays within the next 7 days.
    """
    next_7_days = [
        date.strftime('%d.%m') for date in get_next_7_days(cur_date)
    ]
    return {employee: birthday for employee, birthday in employees_data.items()
            if birthday.strftime('%d.%m') in next_7_days}


def find_youngest_employee(employees_data: dict) -> str:
    """
    Find the youngest employee based on the latest birth date.
    Args:
        employees_data (dict): Dictionary of employees and their birth dates.
    Returns:
        str: The name of the youngest employee.
    """
    key: Callable = employees_data.get
    youngest_employee = max(employees_data, key=key)
    return youngest_employee


def find_youngest_employee_with_birthday_in_next_7_days():
    """
    Find the youngest employee whose birthday is in the next 7 days.
    If no such employee exists, print 'No birthdays planned'.
    """
    current_date = parse_date(input())  # Current date input

    # Collect employee data
    employees_birthdays = collect_employees_data(int(input()))

    # Filter employees with birthdays in the next 7 days
    this_week_birthdays = filter_employees_in_next_7_days(
        current_date, employees_birthdays
    )

    if this_week_birthdays:
        # Print the youngest employee
        print(find_youngest_employee(this_week_birthdays))
    else:
        print('No birthdays planned')


find_youngest_employee_with_birthday_in_next_7_days()
