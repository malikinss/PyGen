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


def read_csv_file(filename: str, delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename (str): Path to the CSV file.
        delimiter (str): The delimiter used in the CSV file (default is ',').

    Returns:
        List[Dict[str, str]]: A list of dictionaries representing the CSV data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the CSV does not contain the required columns.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=delimiter)
            # Ensure the fieldnames are valid
            if not reader.fieldnames or not all(
                col in reader.fieldnames
                for col in ['username', 'email', 'dtime']
            ):
                raise ValueError(
                    "CSV is missing one of the required columns: 'username',"
                    "'email', or 'dtime'."
                )
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise
    except ValueError as e:
        print(f"Error: {e}")
        raise


def count_name_changes_per_user(data: List[Dict[str, str]]) -> Counter:
    """
    Counts the number of name changes per user based on the email.

    Args:
        data (List[Dict[str, str]]): List of dictionaries representing the
        CSV data.

    Returns:
        Counter: A Counter object mapping email addresses to the number
        of name changes.
    """
    emails = [record['email'] for record in data]
    return Counter(emails)


def display_name_changes(changes: Counter) -> None:
    """
    Displays the number of name changes per user in lexicographically sorted
    order.

    Args:
        changes (Counter): Counter object with email addresses and
        corresponding name change counts.
    """
    for email, number_changes in sorted(changes.items()):
        print(f'{email}: {number_changes}')


# Specify the path to the CSV file
input_csv_path = './tests/name_log.csv'

# Main processing flow
try:
    data = read_csv_file(input_csv_path)
    changes = count_name_changes_per_user(data)
    display_name_changes(changes)
except Exception as e:
    # Catch and report any errors encountered during processing
    print(f"An error occurred: {e}")
