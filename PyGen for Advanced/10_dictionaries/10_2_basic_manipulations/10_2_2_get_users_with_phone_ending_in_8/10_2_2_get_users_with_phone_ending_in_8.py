'''
TODO:
    Complete the code below so that it prints the names of all users
    (in alphabetical order) whose user number ends in 8.

NOTE:
    The names must be printed on one line, separated by a space.
'''
from typing import List, Dict


def is_ends_with_8(phone: str) -> bool:
    """
    Check if a phone number ends with the digit '8'.

    Args:
        phone (str): The phone number as a string.

    Returns:
        bool: True if the phone ends with '8', otherwise False.
    """
    return phone.strip()[-1] == '8'


def get_users_with_phone_ending_in_8(users: List[Dict[str, str]]) -> List[str]:
    """
    Get a sorted list of user names whose phone numbers end with '8'.

    Args:
        users (List[Dict[str, str]]): A list of user dictionaries.

    Returns:
        List[str]: A list of sorted user names.
    """
    result = []

    for user in users:
        if is_ends_with_8(user['phone']):
            result.append(user['name'])

    return sorted(result)


# Users data
users = [
    {'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
    {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan@yandex.ru'},
    {'name': 'John', 'phone': '233-421-32', 'email': ''},
    {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
    {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch@gmail.com'},
    {'name': 'Robert', 'phone': '420-2011', 'email': ''},
    {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
    {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'nurmag@gmail.com'},
    {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
    {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
    {'name': 'Maria', 'phone': '12-129-3148', 'email': 'sharapova@gmail.com'},
    {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
    {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}
]

# Get and print result
result = get_users_with_phone_ending_in_8(users)
print(*result)
