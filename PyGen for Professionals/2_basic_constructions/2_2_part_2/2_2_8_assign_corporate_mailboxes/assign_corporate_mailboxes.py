'''
TODO:
    At the BEEGEEK online school, employees are provided with a corporate
    email, which is formed as follows:
        <first name-last name>@beegeek.bzz

    For example,
        timyr-guev@beegeek.bzz

    With this approach, there is a problem of namesakes.

    To solve this problem, it was decided to assign a number to the right.

    Then:
        The first Timur Guev receives the mailbox timyr-guev@beegeek.bzz
            (no number)
        second — timyr-guev1@beegeek.bzz
        the third - timyr-guev2@beegeek.bzz, and so on.

    You are given a list of already occupied boxes in the order in which they
    are issued and the first and last names of new employees in a pre-prepared
    form (in Latin letters with a symbol between them).

    Write a program that distributes corporate boxes to new school employees.

NOTE:
    The input to the program in the first line is a non-negative integer
    n - the number of issued boxes.

    The next n lines list the boxes themselves in order of issue, one per line.

    The next line contains a non-negative integer m — the number of new
    employees to whom corporate boxes need to be distributed.

    Each of the next m lines represents the employee's first and last name in
    ready-to-use format.
'''
from typing import List


def get_list_from_input_strings(strings_quantity: int) -> List[str]:
    """
    Reads a specified number of lines of input and returns them as a list.

    Parameters:
    - strings_quantity (int): The number of lines to read.

    Returns:
    - List[str]: A list of strings.
    """
    return [input().strip() for _ in range(strings_quantity)]


def get_new_email_box(username: str, suffix: str) -> str:
    """
    Generates a new email address by appending a suffix to the username.

    Parameters:
    - username (str): The user's full name in the format 'first-last'.
    - suffix (str): The suffix to be added to the username to form a unique
                    email.

    Returns:
    - str: The new email address.
    """
    return f"{username}{suffix}@beegeek.bzz"


def create_possible_suffixes_pool(size: int) -> List[int]:
    """
    Creates a list of possible suffixes (integers) for the email address.

    Parameters:
    - size (int): The size of the suffix pool.

    Returns:
    - List[int]: A list of possible suffixes.
    """
    return list(range(1, size))


def get_new_suffix(occupied_suffixes: List[int]) -> str:
    """
    Generates a new suffix by finding the smallest unused suffix.

    Parameters:
    - occupied_suffixes (List[int]): A list of suffixes that are already in
                                     use.

    Returns:
    - str: The new suffix as a string.
    """
    possible_suffixes = create_possible_suffixes_pool(20)
    available_suffixes = set(possible_suffixes) - set(occupied_suffixes)

    return str(min(available_suffixes)) if available_suffixes else ''


def get_occupied_suffixes(name: str, occupied_boxes: List[str]) -> List[int]:
    """
    Extracts the suffixes from email addresses that contain the given name.

    Parameters:
    - name (str): The user's full name (first-last).
    - occupied_boxes (List[str]): A list of already occupied email addresses.

    Returns:
    - List[int]: A list of suffixes already assigned to the given name.
    """
    suffixes = []
    for email in occupied_boxes:
        if email.startswith(name):
            suffix_start = len(name)
            suffix_end = email.find('@')
            if suffix_start != suffix_end:
                suffixes.append(int(email[suffix_start:suffix_end]))
    return suffixes


def create_new_emailboxes(
    usernames: List[str], occupied_boxes: List[str]
) -> List[str]:
    """
    Generates new email boxes for the users, ensuring no conflicts with
    existing ones.

    Parameters:
    - usernames (List[str]): A list of users' full names in 'first-last'
                             format.
    - occupied_boxes (List[str]): A list of already occupied email addresses.

    Returns:
    - List[str]: A list of new email addresses assigned to the users.
    """
    new_emailboxes = []
    for name in usernames:
        namesakes_boxes = get_occupied_suffixes(name, occupied_boxes)
        new_suffix = get_new_suffix(namesakes_boxes)
        new_email = get_new_email_box(name, new_suffix)

        occupied_boxes.append(new_email)
        new_emailboxes.append(new_email)

    return new_emailboxes


def assign_corporate_emailboxes() -> List[str]:
    """
    Assigns corporate email addresses to new employees while ensuring no
    duplicates.

    Returns:
    - List[str]: A list of new email addresses assigned to employees.
    """
    occupied_boxes = get_list_from_input_strings(int(input()))
    new_workers = get_list_from_input_strings(int(input()))
    return create_new_emailboxes(new_workers, occupied_boxes)


# Example to run the program
print(*assign_corporate_emailboxes(), sep='\n')
