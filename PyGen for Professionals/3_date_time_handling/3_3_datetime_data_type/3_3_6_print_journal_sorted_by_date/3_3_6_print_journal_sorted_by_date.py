'''
TODO:
    You have access to the text file diary.txt, in which the astronaut wrote
    down small reports for the day.

    He could write each new report either at the beginning of the file, or in
    the middle, or at the end.

    All reports are separated by a blank line.

    Each new report begins with a line with the date and time in the format:
        DD.MM.YYYY; HH:MM
    followed by events that occurred on the specified day.

    Write a program that puts all the astronaut's records in chronological
    order and displays the result.

NOTE:
    When opening a file, use an explicit UTF-8 encoding.

'''
from datetime import datetime
from typing import List, Dict, Optional


def read_data_from_file(file_name: str) -> List[str]:
    """
    Reads data from a file and returns a list of lines.

    Args:
        file_name (str): The path to the file to be read.

    Returns:
        List[str]: A list containing lines of the file.
    """
    try:
        with open(file_name, 'rt', encoding='utf-8') as given_file:
            content = [line.rstrip() for line in given_file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        content = []

    return content


def is_correct_date(day: int, month: int, year: int) -> bool:
    """
    Checks if a given date is valid.

    Args:
        day (int): Day of the month.
        month (int): Month of the year.
        year (int): Year.

    Returns:
        bool: True if the date is valid, otherwise False.
    """
    is_correct_day = 1 <= day <= 31
    is_correct_month = 1 <= month <= 12
    is_correct_year = 1900 <= year <= 9999

    return all([is_correct_day, is_correct_month, is_correct_year])


def is_correct_time(hour: int, minute: int) -> bool:
    """
    Checks if the given time is valid.

    Args:
        hour (int): Hour of the day.
        minute (int): Minute of the hour.

    Returns:
        bool: True if the time is valid, otherwise False.
    """
    is_correct_hour = 0 <= hour <= 23
    is_correct_minute = 0 <= minute <= 59

    return all([is_correct_hour, is_correct_minute])


def is_datetime_as_string(given_string: str) -> bool:
    """
    Validates the given string as a date-time in the format 'DD.MM.YYYY; HH:MM'

    Args:
        given_string (str): The date-time string to validate.

    Returns:
        bool: True if the string is a valid date-time, otherwise False.
    """
    try:
        given_date, given_time = given_string.split('; ')
        day, month, year = map(int, given_date.split('.'))
        hour, minute = map(int, given_time.split(':'))

        correct_date = is_correct_date(day, month, year)
        correct_time = is_correct_time(hour, minute)

        return all([correct_date, correct_time])

    except (ValueError, IndexError):
        return False


def parse_datetime_string(given_string: str) -> Optional[datetime]:
    """
    Parses a date-time string and returns a datetime object.

    Args:
        given_string (str): The date-time string in the format:
                                'DD.MM.YYYY; HH:MM'.

    Returns:
        Optional[datetime]: A datetime object if the string is valid,
                            otherwise None.
    """
    try:
        return datetime.strptime(given_string, '%d.%m.%Y; %H:%M')
    except ValueError:
        print(f"Error: Invalid date-time format - {given_string}")
        return None


def parse_journal_entries(data: List[str]) -> Dict[datetime, List[str]]:
    """
    Parses the journal data and returns a dictionary where the keys
    are datetime objects and the values are lists of journal entries for
    the corresponding date-time.

    Args:
        data (List[str]): A list of strings representing journal entries with
                          date-time stamps.

    Returns:
        Dict[datetime, List[str]]: A dictionary of journal entries sorted
                                   by date-time.
    """
    journal_entries: Dict[datetime, List[str]] = {}
    key: Optional[datetime] = None

    for row in data:
        if is_datetime_as_string(row):
            key = parse_datetime_string(row)
            if key:
                journal_entries[key] = []
        else:
            if key:
                journal_entries[key].append(row)

    return journal_entries


def print_journal_sorted_by_date(journal: Dict[datetime, List[str]]) -> None:
    """
    Prints the journal entries sorted by date-time.

    Args:
        journal (Dict[datetime, List[str]]): A dictionary of journal entries.
    """
    sorted_keys = sorted(journal.keys())
    for record_number, key in enumerate(sorted_keys, start=1):
        print(key.strftime('%d.%m.%Y; %H:%M'))

        value = journal.get(key, [])
        for row in value:
            print(row)

        # Print a blank line between entries, except after the last one
        if record_number != len(sorted_keys):
            print()


def remove_empty_lines(data: List[str]) -> List[str]:
    """
    Removes empty lines from a list of strings.

    Args:
        data (List[str]): The list of strings to filter.

    Returns:
        List[str]: The list without empty lines.
    """
    return [row for row in data if row]


file_path = 'diary.txt'
given_data = read_data_from_file(file_path)
given_data = remove_empty_lines(given_data)
journal_entries = parse_journal_entries(given_data)

print_journal_sorted_by_date(journal_entries)
