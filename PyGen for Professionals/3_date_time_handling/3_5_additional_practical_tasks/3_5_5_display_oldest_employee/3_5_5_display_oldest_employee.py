'''
TODO:
    A list of employees of the organization is given, which indicates their
    last names, given names and dates of birth.

    Write a program that determines the most senior employee from a given list.

    The input to the program in the first line is a natural number n - the
    number of employees working in the organization.

    In the next n lines, data about each employee is entered: first name, last
    name and date of birth, separated by a space.

    Date of birth is indicated in the format DD.MM.YYYY.

    The program should determine the oldest employee and display his date of
    birth, first and last name, separated by a space.

    If there are several such employees, the program should display their date
    of birth, as well as their number, separated by a space.
NOTE:
    It is guaranteed that all employees have different first and last names.
'''

from datetime import datetime, date
from typing import Tuple, List, Dict


DATE_FORMAT = '%d.%m.%Y'


def parse_date(date_string: str) -> date:
    """
    Parses a date string into a date object.

    Args:
        date_string (str): The date string in the format 'DD.MM.YYYY'.

    Returns:
        date: Parsed date object.

    Raises:
        ValueError: If the format is incorrect.
    """
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid date format. Please use DD.MM.YYYY')


def get_employee_info() -> Tuple[str, date]:
    """
    Reads an employee's information from input and returns the full name and
    birth date.

    Returns:
        Tuple[str, date]: A tuple containing the employee's full name and
                          birth date.
    """
    first_name, last_name, birth_date_str = input().split()
    full_name = f"{first_name} {last_name}"
    birth_date = parse_date(birth_date_str)
    return full_name, birth_date


def get_all_employees_info(num_employees: int) -> Dict[str, date]:
    """
    Reads information for multiple employees and stores it in a dictionary.

    Args:
        num_employees (int): The number of employees.

    Returns:
        Dict[str, date]: A dictionary mapping employee names to their
                         birth dates.
    """
    employees_info = {}
    for _ in range(num_employees):
        full_name, birth_date = get_employee_info()
        employees_info[full_name] = birth_date
    return employees_info


def get_earliest_birth_date(employees_data: Dict[str, date]) -> date:
    """
    Finds the earliest (oldest) birth date in the employee list.

    Args:
        employees_data (Dict[str, datetime.date]): Dictionary mapping employee
                                                   names to birth dates.

    Returns:
        datetime.date: The earliest birth date found.
    """
    return min(employees_data.values())


def get_employees_with_birth_date(
    employees_data: Dict[str, date], birth_date: date
) -> List[str]:
    """
    Finds employees who have a specific birth date.

    Args:
        employees_data (Dict[str, date]): Dictionary with employee names as
                                          keys and birth dates as values.
        birth_date (date): The birth date to filter employees by.

    Returns:
        List[str]: A list of employee names who were born on the specified
                   date.
    """
    return [
        name for name, date in employees_data.items() if date == birth_date
    ]


def display_oldest_employee() -> None:
    """
    Reads employee data, finds the oldest employee(s), and prints the result.
    """
    num_employees = int(input())
    employees_data = get_all_employees_info(num_employees)
    oldest_birth_date = get_earliest_birth_date(employees_data)
    oldest_employees = get_employees_with_birth_date(
        employees_data, oldest_birth_date
    )

    if len(oldest_employees) > 1:
        print(oldest_birth_date.strftime(DATE_FORMAT), len(oldest_employees))
    else:
        print(oldest_birth_date.strftime(DATE_FORMAT), oldest_employees[0])


display_oldest_employee()
