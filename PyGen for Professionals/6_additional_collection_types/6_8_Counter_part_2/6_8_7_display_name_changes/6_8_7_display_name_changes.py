'''
TODO:
    You have access to the file name_log.csv, which contains the user name
    change logs.

    The first column contains the changed user name;
    The second column contains the email address;
    The third column contains the date and time of the change;

    However, the user cannot change the email, only the name:
        username,email,dtime
        rare_charles6,charlesthompson@inbox.ru,11/15/2021 08:15
        busy_patricia5,patriciasmith@bk.ru,11/07/2021 08:07
        ...

    Write a program that determines how many times a user has changed their
    name.

    The program should display the email addresses of users, indicating the
    corresponding number of changed names for each.

    Mailboxes should be arranged in lexicographic order, each on a separate
    line, in the following format:
        <email address>: <number of name changes>

NOTE:
    The initial part of the response looks like this:
        barbaraanderson@bk.ru: 3
        barbarabrown@rambler.ru: 3
        barbaradavis@aol.com: 2
        ...
'''

import csv
from collections import Counter
from typing import Dict, List


def read_csv_file(filename: str,
                  delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename: The path to the CSV file.
        delimiter: The delimiter used in the CSV file.

    Returns:
        The content of the CSV file as a list of dictionaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return [row for row in reader]


def count_name_changes_per_user(data: List[Dict[str, str]]) -> Counter:
    """
    Counts the number of name changes per user.

    Args:
        data: List of dictionaries containing CSV data.

    Returns:
        A Counter object with email addresses as keys and the number of name
        changes as values.
    """
    emails = [record['email'] for record in data]
    return Counter(emails)


def display_name_changes(changes: Counter) -> None:
    """
    Displays the number of name changes per user.

    Args:
        changes: Counter object with email addresses and corresponding name
        change counts.
    """
    for email, number_changes in sorted(changes.items()):
        print(f'{email}: {number_changes}')


input_csv_path = '6_8_7/tests/name_log.csv'

data = read_csv_file(input_csv_path, delimiter=',')
changes = count_name_changes_per_user(data)

display_name_changes(changes)
