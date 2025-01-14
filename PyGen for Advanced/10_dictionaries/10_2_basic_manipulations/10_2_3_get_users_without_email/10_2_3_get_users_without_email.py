'''
TODO:
    Complete the code below so that it prints the names of all users
    (in alphabetical order) who do not have email information.

NOTE:
    The email key may not be in the dictionary.
    The names must be printed on one line, separated by a space.
'''
from typing import List, Dict, Any


def get_users_without_email(users: List[Dict[str, Any]]) -> List[str]:
    """
    Returns a list of names of users who do not have email information.
    If the 'email' key is missing or empty, the user is considered
    as not having email.

    Args:
    - users: List of dictionaries containing user information, including
             'name' and 'email'.

    Returns:
    - A list of names sorted in alphabetical order.
    """
    result = []
    for user in users:
        # Check if 'email' key is missing or if it's empty
        if user.get('email', '') == '':
            result.append(user['name'])
    return sorted(result)


# Sample users data
users = [
    {'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
    {'name': 'Helga', 'phone': '555-1618'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
    {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan@yandex.ru'},
    {'name': 'John', 'phone': '233-421-32', 'email': ''},
    {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
    {'name': 'Alina', 'phone': '+7948-799-2434'},
    {'name': 'Robert', 'phone': '420-2011', 'email': ''},
    {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
    {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'nurmag@gmail.com'},
    {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
    {'name': 'Roman', 'phone': '+7459-145-8059'},
    {'name': 'Maria', 'phone': '12-129-3148', 'email': 'sharapova@gmail.com'},
    {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
    {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}
]


# Calling the function and printing the result
result = get_users_without_email(users)
print(*result)
